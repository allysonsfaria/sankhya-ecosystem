---
id: "44011127565335"
titulo: "Por que meus contatos exportados estão sem o número de telefone?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011127565335-Por-que-meus-contatos-exportados-est%C3%A3o-sem-o-n%C3%BAmero-de-telefone"
trilha: "Flowbiz > Campanhas"
atualizado_em: "2026-10-05T18:55:59Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_1193", "sync_hash_d3f7e94e4f54"]
---

# Por que meus contatos exportados estão sem o número de telefone?

## Por que meus contatos exportados estão sem o número de telefone?

Se você tentou exportar uma lista de contatos da Flowbiz e percebeu que muitos deles estão sem a informação de telefone, não se preocupe. Isso geralmente acontece por motivos específicos relacionados à **forma como a lista foi criada** ou à **configuração da sua integração**.

---

Abaixo, explicamos o que pode estar acontecendo de acordo com o tipo de lista que você possui:

### 1. Lista de "Clientes" (Integração via API)

A lista de **Clientes** possui integração direta via API com a sua plataforma de e-commerce e é a principal lista configurada para trazer o número de telefone de forma automática.

Se os telefones estão faltando aqui, existem duas causas prováveis:

- **Importação Inicial:** Quando a sua conta Flowbiz foi criada e a lista inicial de clientes foi importada, a coluna de telefones pode não ter sido incluída no arquivo.
- **Falha no envio dos dados:** A integração da sua plataforma de e-commerce pode não estar enviando o campo de telefone para a Flowbiz no momento da sincronização.

> 💡 **Como resolver?** Se você não tem certeza se a sua plataforma está enviando o telefone via API, entre em contato com o nosso **time de Suporte**. Nós faremos uma análise técnica para avaliar se é possível parametrizar ou corrigir o envio dessa informação.

### 2. Lista de "Assinantes" (Integração via Script)

A lista de **Assinantes** é alimentada através de uma integração via script (geralmente capturando dados de formulários ou pop-ups no seu site).

- Por padrão, essa integração captura apenas dados básicos (como nome e e-mail) e **geralmente não traz o campo de telefone**.
- **A boa notícia:** Se o formulário do seu site coleta o número de telefone dos visitantes, nós podemos configurar a Flowbiz para receber esse dado! Basta solicitar essa parametrização ao nosso suporte.

### 3. Listas de Importação Manual

Se você criou uma lista personalizada e subiu os contatos manualmente na plataforma (via arquivo CSV ou Excel), a Flowbiz só exibirá os telefones se essa informação constava no arquivo original no momento do upload.

- **Como resolver:** Caso tenha esquecido de incluir os telefones, basta fazer uma nova importação atualizando os contatos e garantindo que a coluna de telefone esteja mapeada corretamente.

---

### O que fazer agora?

1. **Verifique a origem da lista:** Identifique se a lista em questão é de Clientes, Assinantes ou Manual.
2. **Fale com o Suporte:** Se for uma lista de Clientes ou Assinantes e você sabe que possui o telefone dos usuários na sua plataforma/site, [abra um chamado com o nosso time de Suporte]. Nós vamos analisar o seu cenário para garantir que esses dados passem a rodar automaticamente para a Flowbiz. 😉

Em caso de dúvidas entre em contato pelo nosso WhatsApp: [(51) 99790-9718](https://ajuda.sankhya.com.br/hc/pt-br/articles/wa.me/5551997909718)
