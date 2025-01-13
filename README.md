# Programação Aplicada 1
Prof. Jefferson Santos

## Projeto 2 (Final) - Dashboard com Streamlit

Nesse projeto vamos construir um Dashboard com a biblioteca [Streamlit](https://streamlit.io/) apresentada nos [vídeos gravados que disponibilizei](https://bit.ly/prog1-pre-gravadas). 

## Arquivo CSV

Para isso necessário definir um conjunto de dados que será usado como base para o que será apresentado no Dashboard. Usaremos o arquivo gerado no Projeto 1 (web scraping) como base para o Projeto 2.

- Se vocês geraram o arquivo no formato CSV, já estão prontos para seguir com o Projeto 2. 
  
- Se o arquivo do Projeto 1 não estiver nesse formato, vocês precisarão ajustar isso primeiro. 
    - Altere o Projeto 1 para que o arquivo gerado seja no formato CSV. 
    - Faça um novo commit e salve com a seguinte mensagem (**obrigatoriamente**):
  `Ajuste no projeto 1 para realização do projeto 2`. Isso vai me permitir identificar a alteração e não considerar sua entrega em atrado no projeto 1. 

**Atenção:**
Se você não entregou o projeto 1, se ele não funcionou ou não conseguiu gerar um arquivo nos moldes descrito acima, você ainda tem uma chance de realizar o projeto 2. Escolha uma base de dados pronta na web e a utilize. Sua nota será descontada (vou avaliar o quanto, caso a caso), mas você ainda terá uma chance de realizar a tarefa final. Você pode utilizar o site **Kaggle**, por exemplo, que disponibiliza uma grande quantidade de dados no formato solicitado para estudo e prática. Neste link, você já obtém varios conjuntos de dados no formtao CSV: https://www.kaggle.com/datasets?fileType=csv. Você pode utilizar outras sites, o Kaggle é só uma dica. 

Ao final, copiem o arquivo CSV (gerado no Projeto 1 ou obtido no Kaggle/Outros) para o codespace do Projeto 2. Lá ele será usado para a elaboração do Dashboard. 

## Dashboard

Vocês devem desenvolver o Dashboard usando a bibloteca Streamlit. Não serão aceitos programas entregues usando outras bibliotecas para o mesmo fim. 

Seu Dashboard deve conter os seguintes elementos: 

- Uma sidebar com ao menos 2 widgets (slider, textbox, checkbox ou selectbox) para filtro e manipulação dos dados. Vocês escolham o que será filtrado ou manipulado. Dei exemplos nos vídeos e vocês também podem consultar a [documentação da biblioteca Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts#widgets).

- Na área principal de conteúdo você deve apresentar:
  - um dataframe exibindo os dados (que se atualizam conforme a manipulação dos widgets da sidebar) 
  - um gráfico a sua escolha feito com os dados apresentados. 

Bom trabalho. 