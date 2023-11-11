import streamlit as st
import pandas as pd
import numpy as np

# Menu utama
menu_utama = st.sidebar.radio("Menu Utama", ["Beranda", "Data Grafik"])

if menu_utama == "Beranda":
    st.title('Aplikasi Streamlit Ujian Akhir Semester')
    st.write("Selamat datang di halaman beranda. Didalam aplikasi ini kami mempunyai 3 jenis data yang berbeda yang nanti nya dapat diakses dengan mudah, diantaranya:")
    st.write("1. Data MLBB Heroes:")
    image = st.image('hero.jpg')
    st.write("2. Data MPL ID Season 10:")
    image = st.image('mpl.jpg')
    st.write("3. Data Rice Production Indonesia")
    image = st.image('rice.jpg')

elif menu_utama == "Data Grafik":
    submenu_tentang = st.sidebar.radio("Pilih Submenu", ["Data Mlbb", "Data MPL", "Rice Production Indonesia"])

    if submenu_tentang == "Data Mlbb":
        st.markdown("<h1 style='text-align: center; font-size: 30px;'>Data Grafik Mlbb</h1>", unsafe_allow_html=True)
        df1=pd.read_csv('Mlbb_Heroes.csv')
        st.write(df1)
        # Widget untuk memilih beberapa hero
        selected_heroes = st.multiselect("Pilih Hero", df1['Name'].unique())
        # Filter data berdasarkan hero yang dipilih
        filter_data = df1[df1['Name'].isin(selected_heroes)]
        # Tampilkan grafik perbandingan HP Regen menggunakan st.bar_chart
        st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Perbandingan HP Regen untuk Hero yang Dipilih:</h2>", unsafe_allow_html=True)
        st.bar_chart(filter_data.set_index('Name')['Hp_Regen'])
        # Filter data kemenangan dan kekalahan berdasarkan hero yang dipilih
        filter_data = df1[df1['Name'].isin(selected_heroes)]
        # Warna yang akan digunakan untuk setiap kategori (menang dan kalah)
        bar_colors = ['#FA8F6F', '#DF312C']
        # Tampilkan grafik bar_chart
        st.markdown("<h2 style='text-align: center; font-size: 20px;'>Perbandingan Kemenangan dan Kekalahan untuk Hero yang Dipilih:</h2>", unsafe_allow_html=True)
        st.bar_chart(filter_data.set_index('Name')[['Esport_Wins', 'Esport_Loss']], use_container_width=True, color=bar_colors)
        st.write("Dari data diatas dapat dijelaskan bahwa grafik yang ditampilkan merupakan grafik untuk menampilkan sebuah perbedaan antara hero satu dengan yang lain.")

    elif submenu_tentang == "Data MPL":
        st.markdown("<h1 style='text-align: center; font-size: 30px;'>Data Grafik MPL ID S10</h1>", unsafe_allow_html=True)
        df2=pd.read_csv('MPL_ID_S10.csv')
        st.write(df2)
        # Widget untuk memilih beberapa hero
        pilih_hero = st.multiselect("Select Heroes", df2['Hero'].unique())
        # Filter data kemenangan dan kekalahan berdasarkan hero yang dipilih
        filtered_data = df2[df2['Hero'].isin(pilih_hero)]
        # Warna yang akan digunakan untuk setiap kategori (menang dan kalah)
        bar_colors = ['#43978D', '#D46C4D']
        # Tampilkan grafik bar_chart
        st.markdown("<h2 style='text-align: center; font-size: 20px;'>Perbandingan Kemenangan dan Kekalahan untuk Hero yang Dipilih:</h2>", unsafe_allow_html=True)
        st.bar_chart(filtered_data.set_index('Hero')[['T_wins', 'T_lose']], use_container_width=True, color=bar_colors)
        st.write("Menampilkan sebuah data dari perbandingan menang dan kalah sesuai dengan hero yang di pilih.")

    elif submenu_tentang == "Rice Production Indonesia":
        st.markdown("<h1 style='text-align: center; font-size: 30px;'>Data Grafik Rice Production Indonesia</h1>", unsafe_allow_html=True)
        df3=pd.read_csv('Rice Production Indonesia 2020-2022.csv')
        st.write(df3)
        # Widget untuk memilih daerah
        selected_provinsi = st.selectbox("Select Provinsi", df3['Provinsi'].unique())
        # Filter data berdasarkan daerah yang dipilih
        filtered_data = df3[df3['Provinsi'] == selected_provinsi]
        # Hitung total produksi untuk setiap tahun
        total_production_per_year = filtered_data.groupby('Year')['Productivity(kw/ha)'].sum()
        # Tampilkan grafik line_chart
        st.markdown(f"<p  style='text-align: center; 'font-size: 18px;'>Hasil Produktivitas: {selected_provinsi} per Tahun</h2>", unsafe_allow_html=True)
        st.bar_chart(total_production_per_year, use_container_width=True)
        # Widget untuk memilih daerah (multiselect)
        selected_provinsi = st.multiselect("Select Provinsi", df3['Provinsi'].unique())
        # Filter data berdasarkan daerah yang dipilih
        filtered_data = df3[df3['Provinsi'].isin(selected_provinsi)]
        # Hitung total produksi untuk setiap tahun dan daerah
        total_produksi = filtered_data.groupby(['Year', 'Provinsi'])['Production.(ton)'].sum().unstack()
        # Tampilkan grafik line_chart
        st.markdown("<h2 style='text-align: center; font-size: 20px;'>Perbandingan Hasil Produksi per Tahun untuk Daerah yang Dipilih:</h2>", unsafe_allow_html=True)
        st.bar_chart(total_produksi, use_container_width=True)
        st.write("Dalam grafik hasil produksi beras di indonesia menampilkan sebuah perbandingan produksi dan produktivitas sebuah provinsi dari tahun 2020 - 2022.")