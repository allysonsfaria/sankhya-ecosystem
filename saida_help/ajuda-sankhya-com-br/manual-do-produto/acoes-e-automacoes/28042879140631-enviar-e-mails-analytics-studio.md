---
id: "28042879140631"
titulo: "Enviar E-mails - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28042879140631-Enviar-E-mails-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Ações e automações"
atualizado_em: "2026-09-23T17:38:36Z"
rotulos: ["Configuração", "Relatórios", "E-mail", "Analytics Studio", "Automação"]
---

# Enviar E-mails - Analytics Studio

O passo de ação Enviar E-mails permite automatizar o envio de e-mails personalizados para diferentes destinatários, utilizando dados dinâmicos extraídos de uma View configurada. Esse passo é ideal para enviar relatórios, notificações, ou qualquer outro tipo de comunicação que precise ser adaptada com base em informações específicas de cada destinatário.

![Imagem 1: O passo de ação Enviar E-mails permite automatizar o envio de e-mails personalizados para diferentes destinatários,…](https://ajuda.sankhya.com.br/hc/article_attachments/28042879137303)

### Configurando a View

Qualquer tipo de View pode ser utilizado para alimentar os dados necessários para a criação de e-mails:

- View de Análise de Dados
- View de Cadastro
- View de SQL

**Vinculação de Cadastro (aplicável para VIEW de SQL):** ao utilizar uma View de SQL, é fundamental vincular o cadastro utilizado na sua query. Isso é necessário para que o sistema consiga filtrar corretamente os dados e aplicar as variáveis na geração dos e-mails, especialmente ao utilizar links dinâmicos.

### Configuração de campos dinâmicos

Após configurar a View, um preview do resultado será exibido. Nesse momento, as colunas da View podem ser usadas para definir os campos dinâmicos do e-mail:

**![Imagem 2: Destinatário (E-mail): selecione a coluna da View que contém o e-mail do destinatário. Cada linha da VIEW corresponderá…](https://ajuda.sankhya.com.br/hc/article_attachments/28043219345559) Destinatário (E-mail):** selecione a coluna da View que contém o e-mail do destinatário. Cada linha da VIEW corresponderá a um e-mail enviado.

**![Imagem 3: Assunto do E-mail: pode ser uma combinação de texto fixo e variáveis da View. Exemplo: "Olá, $Nome" personaliza o…](https://ajuda.sankhya.com.br/hc/article_attachments/28043203944087) Assunto do E-mail:** pode ser uma combinação de texto fixo e variáveis da View. Exemplo: "Olá, $Nome" personaliza o assunto para cada destinatário.

**![Imagem 4: Corpo do E-mail: assim como o assunto, o corpo do e-mail pode misturar texto fixo com variáveis provenientes das…](https://ajuda.sankhya.com.br/hc/article_attachments/28043203944855) Corpo do E-mail:** assim como o assunto, o corpo do e-mail pode misturar texto fixo com variáveis provenientes das colunas da View. Cada linha da View representará um e-mail personalizado.

#### Formatação de texto

Ao editar o corpo do e-mail, estão disponíveis várias opções de formatação, como:

- Negrito e itálico;
- Ajuste do tamanho da fonte;
- Bullets e numerais;
- Hiperlinks: útil para a variável $Link. Por exemplo, é possível inserir "clique aqui" como hiperlink para o link dinâmico, evitando expor a URL completa no e-mail.

### Link dinâmico

Ao clicar na opção **"Link Dinâmico"**, é possível escolher uma pasta e uma tela dentro do [Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231). O sistema gerará automaticamente um link dinâmico, identificado como a variável $Link. Esse link pode ser inserido no corpo do e-mail, permitindo que o destinatário acesse diretamente uma tela específica no Analytics AI sem precisar fazer login. O link é filtrado conforme os dados da linha correspondente, garantindo que cada usuário acesse apenas as informações relevantes para ele.

### Importância da vinculação de cadastro na View de SQL

Ao utilizar uma View de SQL, é crucial vincular o cadastro correspondente ao ID relevante, como o ID do vendedor, por exemplo. Essa vinculação garante que o link dinâmico funcione corretamente, filtrando os dados para que cada destinatário acesse apenas suas próprias informações na tela dinâmica aberta pelo link.

Ao utilizar uma View de SQL, a vinculação com o cadastro correspondente (como o ID do vendedor) é indispensável. Isso assegura que o link dinâmico funcione corretamente, aplicando os filtros necessários para que cada destinatário visualize apenas os dados relacionados a ele.

### Exemplo de uso

Imagine um cenário de envio semanal de e-mails para vendedores. O e-mail pode incluir uma saudação personalizada, o resumo das vendas da semana e um link para um painel interativo onde o vendedor pode analisar seus dados em mais detalhes. Por exemplo:

```
Olá, $Nome,

Você vendeu $TotalVendas na última semana.

[Clique aqui]($Link) para ver o painel interativo e analisar suas vendas.
```

---

![Imagem 5: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28108222415383) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
