---
id: "42427251011607"
titulo: "Como cadastrar um empregador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427251011607-Como-cadastrar-um-empregador"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:30:00Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a33ee3baacdb0bbc16303ea", "sync_hash_5a611d8e0b47"]
---

# Como cadastrar um empregador

Neste artigo, vamos mostrar como cadastrar um novo **empregador** na plataforma Pontotel de forma rápida e eficiente. Esse processo é essencial para garantir que todos os dados dos empregadores estejam organizados desde o início, facilitando a gestão e o acompanhamento do seu time. Com as informações registradas corretamente, você terá uma base estruturada para aproveitar ao máximo as demais funcionalidades da plataforma.
Por padrão, a empresa principal informada durante a contratação já estará cadastrada na plataforma. No entanto, também é possível cadastrar novos empregadores.

Neste artigo, veremos como realizar esse cadastro.

---

## Como cadastrar um empregador

1. No menu de navegação do[site Gestão](https://gestao.pontotel.com.br/), clique em **Cadastros** e, em seguida, selecione **Empregadores**.
2. Clique em **Criar novo empregador**.
3. Preencha os campos necessários:

![Imagem 1: Preencha os campos necessários:](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_7nsjow.png)

- **Razão Social:** Campo obrigatório, que deverá conter a razão social da empresa ou nome completo do empregador, caso seja pessoa física.
- **CNPJ** ou **CPF:** Deve ser preenchido obrigatoriamente um dos dois, a depender se o empregador é pessoa jurídica ou física.
- **Nome fantasia:** Campo opcional, que pode ser preenchido com o nome da empresa como é conhecida no dia a dia.
- **Código:** Use este campo para inserir um identificador único para o empregador, geralmente como ele é identificado também no sistema de folha. Isso é especialmente importante para clientes com mais de um CNPJ, pois ajuda a organizar e diferenciar os cadastros quando for levar informações para outro sistema através do E02, facilitando a consulta e o gerenciamento no dia a dia.
- **CEI/CNO/CAEPF:** Campo opcional, destinado ao número de registro do empregador junto ao INSS ou à Receita Federal.
- **Logo do empregador:** Pode ser inserida a logotipo da empresa, em formato JPG ou PNG. Caso tenha adicionado, a logotipo aparecerá os espelhos de ponto dos colaboradores vinculados ao empregador. Caso não insira, o espelho de ponto refletirá com a logo da Pontotel.

4. Depois de preencher os campos, clique em **Salvar**.

---

## ✨ Novidade: Suporte ao CNPJ alfanumérico

A partir de julho de 2026, a Receita Federal passa a emitir CNPJs no formato alfanumérico, que combina letras e números. O cadastro de empregador da Pontotel já reconhece e valida o novo padrão.
O campo de CNPJ aceita valores com 12 caracteres alfanuméricos (letras de A a Z e números de 0 a 9), seguidos de 2 dígitos verificadores numéricos, no formato AA.AAA.AAA/AAAA-DV.

Veja como isso funciona na prática:

- CNPJs numéricos continuam valendo: todos os empregadores já cadastrados com CNPJ tradicional seguem funcionando normalmente. Você não precisa alterar nada, e não há impacto em relatórios, exportações ou integrações.
- Digite com ou sem máscara: o campo aceita o CNPJ com ou sem pontos, barra e traço.
- Letras minúsculas são ajustadas automaticamente: se você digitar o CNPJ em letras minúsculas, o sistema converte para maiúsculas antes de validar e salvar o cadastro.
- Mensagens de erro mais claras: se o valor digitado não seguir o padrão da Receita Federal, o sistema exibe "CNPJ possui formato inválido". Se o formato estiver certo, mas os dígitos verificadores não conferirem, a mensagem exibida é "Dígito verificador incorreto".

O novo formato é aceito em toda a plataforma: site Gestão, Bateponto Web, aplicativos e API Pública.

> 💡 Dica: a validação do CNPJ alfanumérico verifica o formato e os dígitos verificadores. O sistema não consulta a situação cadastral da empresa junto à Receita Federal.

---

> 💡 Dica: A Pontotel conta com o Tour Guiado, uma funcionalidade interativa disponível dentro do próprio site Pontotel Gestão, criada para auxiliar você na configuração de cadastros, parametrizações e utilização das principais ferramentas da plataforma. Com orientações passo a passo diretamente na tela, o Tour ajuda a tornar o processo mais simples, rápido e intuitivo, reduzindo dúvidas e evitando erros durante as configurações. Sempre que precisar, você poderá ativar a funcionalidade em: Admin > Tour. Para mais detalhes sobre como utilizar o recurso, confira o artigo: [Como utilizar o Tour Guiado](https://sankhya.zendesk.com/hc/pt-br/articles/42427249823127).

---

Pronto! Com o empregador cadastrado, você tem uma base bem estruturada para gerenciar e organizar os seus cadastros. Isso garante que as demais funcionalidades da plataforma possam ser usadas de forma completa e eficiente, ajudando você a manter um acompanhamento preciso das jornadas e do desempenho do seu time.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
