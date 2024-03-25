import streamlit as st
import subprocess

txt_path = st.text_area(
  label = "Escreva o caminho para o arquivo de texto",
  height = 5,
  max_chars = 200,
  placeholder = "O arquivo deve ser em formato .txt"
)

pref = st.text_area(
  label = "Escreva os prefixos para pesquisar no texto",
  height = 5,
  max_chars = 50,
  placeholder = "Escreva os prefixos separados por espaços"
)

if pref != '' and txt_path != '':
  prefix_list = pref.split(' ')
  arg = ["python", "search.py"]
  arg.append(txt_path)
  for i in prefix_list:
    arg.append(i)

  subprocess.run(arg)

  file = open("words_found.txt", 'r')
  words_found = file.read()

  st.write(words_found)