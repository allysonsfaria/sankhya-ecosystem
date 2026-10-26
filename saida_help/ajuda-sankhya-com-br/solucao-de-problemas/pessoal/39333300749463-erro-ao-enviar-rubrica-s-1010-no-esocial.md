---
id: "39333300749463"
titulo: "Erro ao Enviar Rubrica S-1010 no eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39333300749463-Erro-ao-Enviar-Rubrica-S-1010-no-eSocial"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:39Z"
rotulos: ["Folha", "eSocial", "Central do eSocial", "S-1010", "Erro", "Artigo criado KCS", "Sankhya RH - KCS", "Rubrica"]
---

# Erro ao Enviar Rubrica S-1010 no eSocial

**MENSAGEM**

**Erro 269:** Rubrica de código 'XXXXX' e identificador de tabela 'XXXXX' não existe no cadastro do empregador para o período 'AAAA-MM'.

**SITUAÇÃO**

Esses erros ocorrem durante o envio do evento S-1010 (Tabela de Rubricas) ao eSocial, geralmente nas seguintes situações:

• Ao tentar enviar rubricas novas ou alteradas durante o fechamento da folha de pagamento.
• Quando há inconsistência na data de início de validade da rubrica.
• Ao utilizar códigos de incidência tributária inválidos ou incompatíveis com as tabelas do eSocial.
• Quando a rubrica não foi previamente cadastrada no portal do eSocial para o período de apuração.
• Durante o envio do evento S-1200 (Remuneração) que depende do S-1010.

**SOLUÇÃO**

**Erro 269 - Rubrica Não Existe no Cadastro:**

**(1)**Verifique no portal do eSocial se a rubrica informada consta no cadastro do empregador para o período de apuração.

**(2)**Caso a rubrica não esteja cadastrada, acesse a tela **"Central eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e gere o **S-1010** para a rubrica específica.

**(3)**Desmarque a opção **"Utilizar a data de início padrão do sistema"** e informe a data de validade correspondente ao período de apuração (exemplo: 01/11 para competência 11/2025).

![Imagem 1: (3) Desmarque a opção "Utilizar a data de início padrão do sistema" e informe a data de validade correspondente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/41466124710551)

**(4)**Envie o **S-1010** e aguarde a recepção com sucesso.

**(5)**Após a recepção do **S-1010**, realize o envio do evento **S-1200** (Remuneração) normalmente.

**Para Rubricas com Natureza Inválida:**

**(1)**Consulte o leiaute das tabelas 1.3 do eSocial para verificar a data de início de validade da natureza da rubrica utilizada.

**(2)**Desabilite a flag **"Envio com data padrão do sistema"** e informe uma data de início de validade compatível com a natureza da rubrica.

![Imagem 2: (2) Desabilite a flag "Envio com data padrão do sistema" e informe uma data de início de validade compatível com a…](https://ajuda.sankhya.com.br/hc/article_attachments/41466124710551)

**(3)**Gere e envie novamente o **S-1010**.

**CAUSA**

**Erro 269:** A rubrica utilizada no cálculo da folha não foi previamente enviada ao eSocial através do evento **S-1010** para o período de apuração correspondente, ou foi enviada com data de validade incompatível.

**Natureza Inválida:** A natureza da rubrica possui uma data de início de validade específica no leiaute do eSocial, e o envio está sendo realizado com data anterior à permitida para aquela natureza.
