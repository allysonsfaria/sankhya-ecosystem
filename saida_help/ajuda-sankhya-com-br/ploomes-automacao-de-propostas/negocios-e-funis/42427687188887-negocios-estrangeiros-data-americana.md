---
id: "42427687188887"
titulo: "Negócios Estrangeiros - Data Americana."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427687188887-Neg%C3%B3cios-Estrangeiros-Data-Americana"
trilha: "PLOOMES: Automação de propostas  > Negócios e funis"
atualizado_em: "2026-08-03T13:06:20Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452179", "sync_hash_36217a8d09af"]
---

# Negócios Estrangeiros - Data Americana.

Nesse artigo você encontrará algumas dicas e passo a passo sobre: Data Americana.

- **Data Americana:**

No cotidiano você poderá se deparar com um cliente estrangeiro que possui um Negócio em andamento e deseja que na proposta conste a data no formato americano (mês/dia/ano).

Para isso, precisamos ir em: Negócios > Ver Todos os Funis > Selecionar o Funil > Clicar na Caneta > Formulário de Novo Negócio > Adicionar Campo > Criar Campo do Tipo **Texto Simples** > Nome do Campo: **Data Americana >** Configurações Avançadas > Fórmula > Configurar > Fórmula Simples - iremos inserir:

var date = "**INSERIR O CAMPO DE NEGÓCIO INÍCIO**"

var ano = date.split("T")[0].split("-")[0];

var mes = date.split("T")[0].split("-")[1];

var dia = date.split("T")[0].split("-")[2];

var concatenado = mes + "/" + dia + "/" + ano;

concatenado

**Dica:** podemos utilizar como gatilho uma informação do Negócio que sempre é preenchida, como por exemplo o Título.

Depois basta salvar a fórmula, criação de campos e o formulário.

**Informação Importante:** a Data Americana será aplicada automaticamente apenas para novos negócios ou antigos deverão ser inseridos manualmente.

- **Data Americana no Modelo da Proposta:**

Se você quiser inserir a Data Americana no Modelo da Proposta, precisará ir em: Administração > Modelos de Documento > Selecionar o Modelo da Proposta > Campos > Negócios > Inserir o Campo de Data Americana.

**Clique aqui para visualizar um vídeo com a demonstração e passo a passo desse processo:**

**[Vídeo Demonstrativo](https://ploomesov2d9p.hippovideo.io/video/play/rWA4M2Hu7sU2QrYAbk_Eb7SDzFowp1V-hGIcc5xOGY0?utm_source=hv-campaigns&hreferer=private&_=1616795479771)**
