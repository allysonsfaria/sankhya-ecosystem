---
id: "43547990323095"
titulo: "ERRO: A tabela de CST (TLFCSTIC) para IBS/CBS não está atualizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547990323095-ERRO-A-tabela-de-CST-TLFCSTIC-para-IBS-CBS-n%C3%A3o-est%C3%A1-atualizada"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-09-29T12:08:49Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# ERRO: A tabela de CST (TLFCSTIC) para IBS/CBS não está atualizada

#### SITUAÇÃO

Ao tentar importar ou cadastrar alíquotas de IBS/CBS nas telas específicas do sistema, o usuário se depara com uma mensagem de erro informando que a tabela de CST (TLFCSTIC) não está atualizada. O erro ocorre durante o processo de inclusão ou atualização de alíquotas relacionadas à reforma tributária, impedindo a continuidade do cadastro.

#### SOLUÇÃO

**(1)** A atualização das tabelas da Reforma Tributária é feita diretamente pela rotina, utilizando a opção **“Outras Opções” → “Atualizar Tabelas RTC”**, conforme apresentado na imagem.

![Imagem 1: (1) A atualização das tabelas da Reforma Tributária é feita diretamente pela rotina, utilizando a opção “Outras Opções”…](https://ajuda.sankhya.com.br/attachments/token/cMjSFWAlOnUDCFD6Td9nKKMkL/?name=image.png)

**(2)** Obs.: Esse job é processado automaticamente uma vez por mês. Já a atualização manual deve ser feita apenas em casos excepcionais, pois só pode ser executada uma vez a cada 7 dias.

#### CAUSA

A causa do erro é a ausência de atualização da tabela de CST (TLFCSTIC) e da tabela de classificação tributária (CCLASSTRIB) no banco de dados do sistema.
