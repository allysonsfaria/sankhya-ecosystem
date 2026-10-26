---
id: "28045273039255"
titulo: "Imagem - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28045273039255-Imagem-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Componentes"
atualizado_em: "2026-09-23T17:12:10Z"
rotulos: ["Configuração", "Componentes", "Analytics Studio", "Imagem"]
---

# Imagem - Analytics Studio

O componente Imagem é utilizado para exibir imagens estáticas ou dinâmicas, provenientes do banco de dados. Este componente é ideal para diversos contextos, como exibir fotos de produtos em uma lista de produtos, mostrar avatares de colaboradores em uma lista de equipe, ou para criar interfaces visualmente atrativas.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=U8sbg2YPTpI)

### Como configurar

**Arraste para a tela:** arraste o componente Imagem para a tela onde deseja exibir a imagem.

**Configurar a VIEW:** configure a View através de SQL, View Análise de Dados ou View de Cadastro caso queira que a imagem seja dinâmica e provenha do banco de dados. A View deve retornar o valor da URL da imagem desejada na primeira coluna e primeira linha.

### Personalizar

#### Configurações gerais

**Imagem:** pode-se definir uma imagem estática ou o endereço do arquivo diretamente. Para tornar a imagem dinâmica, ative a marcação **"Definir imagem com base em VIEW"**, que fará com que a imagem seja carregada a partir da URL retornada pela VIEW.

**Manter Proporção:** padrão que mantém a proporção da imagem dentro do espaço do componente.

**Formato da Imagem:**

- **Cobrir:** a imagem cobre todo o componente, mantendo a proporção e aplicando um efeito de zoom para preencher o espaço.
- **Formas:**
  - **Círculo:** exibe a imagem em formato circular.
  - **Quadrado:** exibe a imagem em formato quadrado.
  - **Quadrado com Bordas Suaves:** exibe a imagem em formato quadrado com cantos arredondados.

#### Animação

As opções de animação incluem:

- **Transição:** ative para adicionar um efeito de mudança ao passar o cursor sobre a imagem.
- **Cor da Transição:** defina a cor de fundo durante a transição.
- **Elevação:** ative para adicionar um efeito de sombreamento que adiciona profundidade à imagem.
- **Nível da Elevação:** defina o nível de profundidade da elevação.

#### Visibilidade dinâmica

A funcionalidade de Visibilidade Dinâmica permite que a imagem fique visível ou invisível conforme o valor retornado por uma View. A imagem desaparecerá se o valor retornado for 0 ou null e aparecerá para qualquer outro número. Esta funcionalidade pode ser aplicada utilizando a View do próprio componente ou a View da tela, oferecendo flexibilidade na configuração e controle do comportamento dos componentes.

- **Referenciando a VIEW do próprio componente:** baseia-se na primeira linha e coluna retornada pela View para determinar a visibilidade.
- **Referenciando a VIEW da tela:** utilize comandos de variáveis, como "$A1", para pegar o valor da primeira linha e coluna da View da tela.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=U6LvjX8fghE)

#### Reatividade

Assim como no componente Label, a Imagem também pode ser configurada para atualizar manualmente componentes específicos quando necessário. Para mais informações, consulte o artigo [Reatividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/28080172417687-Reatividade-Analytics-Studio).

### Interações

A Imagem aceita as seguintes interações:

- **Ação:** permite definir uma ação para ser executada ao interagir com a imagem.
- **Ação de Database:** possibilita realizar operações de manipulação de dados, como INSERT, UPDATE, DELETE, ou chamar PROCEDURES.
- **Formulário:** permite abrir um formulário ao interagir com a imagem.
- **Modal:** permite abrir um modal ao interagir com a imagem.

---

![Imagem 1: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28131863670423) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
