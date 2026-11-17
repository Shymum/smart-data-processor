import streamlit as st
from processor import read_table, clean_table, combine_tables, to_xlsx

st.set_page_config(page_title='Smart Data Processor', page_icon='📊', layout='wide')
st.title('📊 Smart Data Processor')
st.caption('Upload, combine and clean tabular data locally.')
files = st.file_uploader('CSV or XLSX files', type=['csv', 'xlsx'], accept_multiple_files=True)
if files:
    frames = []
    for file in files:
        try:
            frame = read_table(file, file.name)
            frames.append(frame)
            with st.expander(f'{file.name} — {len(frame)} rows', expanded=len(files) == 1):
                st.dataframe(frame.head(100), use_container_width=True)
        except Exception as exc:
            st.error(f'Could not read {file.name}: {exc}')
    if frames:
        st.subheader('Clean and combine')
        st.caption('Files are stacked by column name; missing columns become empty cells.')
        trim = st.checkbox('Trim text and treat blank text as missing', value=True)
        empty = st.checkbox('Remove completely empty rows', value=True)
        duplicates = st.checkbox('Remove duplicate rows', value=True)
        combined = combine_tables(frames)
        result = clean_table(combined, trim, empty, duplicates)
        st.write(f'{len(combined)} input rows → {len(result)} output rows')
        st.dataframe(result, use_container_width=True)
        st.download_button('Download CSV', result.to_csv(index=False).encode('utf-8-sig'), 'cleaned.csv', 'text/csv')
        st.download_button('Download XLSX', to_xlsx(result), 'cleaned.xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
else:
    st.info('Try the synthetic files in the demo_data folder.')
