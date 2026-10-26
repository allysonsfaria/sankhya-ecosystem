---
id: "360043577994"
titulo: "Base de numeração da TOP marcada para manual e o número não foi informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577994-Base-de-numera%C3%A7%C3%A3o-da-TOP-marcada-para-manual-e-o-n%C3%BAmero-n%C3%A3o-foi-informado"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-08-01T01:24:00Z"
rotulos: ["#PUBLIFER", "CORE_E02951", "Configuração", "Nota Fiscal", "TOP", "Financeiro", "Numeração manual e automática", "Base de numeração da TOP", "Controle de numeração e cadastro", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# Base de numeração da TOP marcada para manual e o número não foi informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16107711128599) MENSAGEM:**

[CORE\_E02951] Base de Numeração da TOP marcada para Manual e o número não foi informado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16107695847191) SOLUÇÃO:**

Para resolver este erro, escolha uma das opções abaixo:

![Imagem 3: Opção 1: Informar o número da nota manualmente](https://ajuda.sankhya.com.br/hc/article_attachments/16107711131799)**Opção 1: Informar o número da nota manualmente**

Se a numeração dessa operação é mesmo manual, abra a nota, acesse o cabeçalho e preencha o campo "Nro. Nota" **antes de confirmá-la**. 

![Imagem 4: Se a numeração dessa operação é mesmo manual, abra a nota, acesse o cabeçalho e preencha o campo "Nro. Nota" antes de…](https://ajuda.sankhya.com.br/hc/article_attachments/14528959804823)

(2)** Opção 2: Tornar a numeração automática**

Se o número deveria ser gerado pelo sistema, ajuste o cadastro da TOP:

1. Em "Tipo de Operação – TOP", acesse a aba "Impressão".
2. Altere "Base de Numeração" e "Tipo de Numeração" para a opção correta da sua operação (qualquer uma diferente de "Manual").
3. Em "Outras Opções" » "Controle de Numeração", verifique se já existe controle cadastrado para a empresa/série/modelo da nota. Se não existir, cadastre um novo marcando a opção "Numeração Automática".

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16107695856919) CAUSA:**

A TOP usada na nota está com o campo "Base de Numeração" (aba Impressão) marcado como "Manual (Informada pelo Usuário)". Nesse caso, o número precisa ser digitado pelo usuário antes de confirmar a nota, o sistema não gera automaticamente.

Esse erro pode ocorrer em qualquer operação vinculada a uma TOP com essa configuração: Central de Compras, Produção, devoluções e outras rotinas fiscais.

**Observação:** se não tiver certeza de qual configuração fiscal se aplica à sua operação, peça apoio de alguém com conhecimento fiscal antes de alterar a TOP, essa configuração afeta a numeração oficial dos documentos.
