---
id: "27061199058967"
titulo: "Erro MS1459 - Não é permitido o envio de mais de um evento para o contribuinte, num mesmo período de apuração, mesmo estabelecimento adicionador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27061199058967-Erro-MS1459-N%C3%A3o-%C3%A9-permitido-o-envio-de-mais-de-um-evento-para-o-contribuinte-num-mesmo-per%C3%ADodo-de-apura%C3%A7%C3%A3o-mesmo-estabelecimento-adicionador"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:40:14Z"
rotulos: ["Configuração", "SEFAZ", "EFD", "Erro MS1459", "Não é permitido o envio de mais de um evento para o contribuinte", "num mesmo período de apuração mesmo estabelecimento adicionador", "Erro", "Documentos Eletrônicos", "Reinf"]
---

# Erro MS1459 - Não é permitido o envio de mais de um evento para o contribuinte, num mesmo período de apuração, mesmo estabelecimento adicionador

O Erro ocorre quando se tenta enviar mais de um evento ou documento fiscal com a mesma natureza de evento, período de apuração e para o mesmo CNPJ base ou filial, em um sistema de obrigações acessórias como o  **REINF**.

A causa desse erro é que o evento R1000 é enviado apenas uma vez, e qualquer alteração nos registros requer o envio do R1000 novamente com o tipo de envio **"Alteração".**

**Exemplo:**

Suponha que tenha acontecido a mudança de sistema e agora o cliente usará o Sankhya. E a data que vai começar usar o envio pelo Sankhya é na referencia 01/09/2024. Então, no Ecac, deve ser informado como data Fim no R1000 a data 01/08/2024.

No Ecac o R1000 sempre fica aberto, somente quando muda de sistema ou se por algum motivo for necessário fazer um novo envio do R1000.

Nesse caso, a data fim deve ter sido informada no R1000 dentro do Ecac.

- Consulte o último registro do evento R1000 no Ecac;
- Verifique o intervalo entre a Data Inicial da Vigência e a Data Final da Vigência;
- Se necessário informe a data fim sendo ela a última referência não enviada pelo Sankhya.

(1)**Configuração no Sistema**

Na tela  **"Empresa"** (Comercial » Preferências » Empresa), aba **"EFD-Escrituração Fiscal Digital"**, selecione o tipo de escrituração como **"EFD Reinf".** No campo **"Data Validade Inicial Reinf"** informe a referência que vai acontecer o primeiro envio pelo Sankhya.

**![Imagem 1: Deixe o campo "Data Validade Final Reinf" vazio](https://ajuda.sankhya.com.br/hc/article_attachments/27120498493975) Deixe o campo "Data Validade Final Reinf" vazio**

Após ajustar as datas, transmita novamente o evento R1000 para que as datas de vigência fiquem compatíveis com a referência atual.
