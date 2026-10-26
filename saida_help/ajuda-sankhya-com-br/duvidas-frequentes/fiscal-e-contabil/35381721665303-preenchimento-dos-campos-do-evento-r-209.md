---
id: "35381721665303"
titulo: "Preenchimento dos campos do evento R-2099"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35381721665303-Preenchimento-dos-campos-do-evento-R-2099"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:25:14Z"
rotulos: ["Configuração", "Impostos", "eSocial", "Preenchimento", "evento R-2099", "evento", "REINF", "dos campos", "R-2099", "ID do Evento", "eCAC", "CGC", "Documentos Eletrônicos"]
---

# Preenchimento dos campos do evento R-2099

Este artigo descreve as regras de preenchimento dos principais campos do evento R-2099, visando documentar e padronizar as regras adotadas pelo sistema na geração do arquivo para envio ao ambiente REINF.

(1)** ID do Evento:** Deve ser construído conforme as regras abaixo:

(1)** Prefixo:** Inicia-se sempre com “ID”.

(1)** Tipo de CGC:** Em seguida, é indicado o tipo de CGC da empresa:

1 para CNPJ;

2 para CPF.

(1)** Identificação da Empresa:**

Na tela **“Preferências da Empresa”** (Comercial » Preferências » Empresa), aba **“REINF”**, caso o tipo de registro seja CNPJ e o campo **“Empresa de Adm. Pública Direta?”** esteja marcado, será utilizado o CNPJ completo da empresa.

Caso o campo não esteja marcado, o sistema utilizará os 8 primeiros dígitos do CNPJ e preencherá os 6 dígitos restantes com zeros, completando os 14 dígitos.

Se for CPF, o sistema utilizará os 11 dígitos do CPF, completando com zeros à direita até atingir 14 dígitos.

(1)** Data e Hora:** Em seguida, será adicionada a data e hora da geração no formato YYYYMMDDHH24MISS (hora no padrão de 0 a 23).

(1)** Sequência:** Por fim, serão incluídos os dígitos correspondentes à sequência de geração do evento.

(2)** Nro. do Recibo:** será o retorno do evento junto ao eCAC;

(3)** Tipo de Inscrição:** Sistema valida se a quantidade de dígitos do CGC da empresa é 14, sendo, será informado 'CNPJ' caso contrário, CPF;

(4)** Nro. de Inscrição:** Sistema valida se o CGC da empresa tem 14 dígitos, havendo, valida se e o campo Empresa de Adm. Pública Direta? não está marcado, assim apresentará em tela, os 8 primeiros dígitos do CNPJ, caso contrário, apresentará todo o CGC da empresa;

**(5)** **Os campos** >> **Nome do Responsável,** **CPF do Responsável, Telefone e E-mail: esses** campos serão preenchidos pelos dados do parceiro informado no campo "**Responsável pela Entrega**". 

Os campos abaixo serão preenchidos se houver algum evento para os respectivos eventos **R2010, R2020, R2030, R2040, R2050, R2055, R2060 e R2070**:  

- Contratou serviços sujeitos à retenção de contribuição previdenciária?
- Prestou serviços sujeitos à retenção de contribuição previdenciária?
- A associação desportiva possui informações sobre recursos recebidos?
- A associação desportiva possui informações sobre repasses efetuados?
- O Produtor Rural PJ/Agroindústria possui informações de comercialização de produção?
- Possui informações sobre a apuração da Contribuição Previdenciária sobre a Receita Bruta?
- Possui informações sobre aquisição de produção rural de pessoas físicas?
- Possui informações de pagamento diversos no período de apuração? (SISTEMA NÃO GERA R2070)
- Competência sem movimento: Campo com preenchimento somente até 2018;
- Usuário responsável pelo fechamento: código do usuário logado que realizou o fechamento;
