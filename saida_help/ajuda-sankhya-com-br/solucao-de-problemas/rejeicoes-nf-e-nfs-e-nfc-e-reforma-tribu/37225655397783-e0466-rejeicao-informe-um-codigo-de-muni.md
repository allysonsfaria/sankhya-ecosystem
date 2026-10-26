---
id: "37225655397783"
titulo: "E0466 Rejeição: Informe um código de município existente para o documento de nota, conforme tabela de municípios do IBGE."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225655397783-E0466-Rejei%C3%A7%C3%A3o-Informe-um-c%C3%B3digo-de-munic%C3%ADpio-existente-para-o-documento-de-nota-conforme-tabela-de-munic%C3%ADpios-do-IBGE"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:44Z"
rotulos: ["Configuração", "NF-e", "Cidades", "SEFAZ", "IBGE", "Erro", "Código do município", "Documento fiscal eletrônico (NF-e NFC-e ou CT-e)", "Código de município existente para o documento de nota", "Código oficial do município"]
---

# E0466 Rejeição: Informe um código de município existente para o documento de nota, conforme tabela de municípios do IBGE.

**MENSAGEM**

E0466 Rejeição: Informe um código de município existente para o documento de nota, conforme tabela de municípios do IBGE.

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e, NFC-e ou CT-e), o sistema rejeitou a nota apresentando a mensagem de erro **E0466**.

**SOLUÇÃO**

Para corrigir esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços) e localize o município que está sendo utilizado no documento fiscal rejeitado.

**(2)** Verifique se o campo **"Mun. domicílio fiscal"** está preenchido corretamente. Este campo deve conter o **código oficial do município** conforme a tabela do IBGE.

**(3)** Acesse o site oficial do IBGE para consultar o código correto do município:

- Acesse o site oficial do [**''IBGE''**](https://cidades.ibge.gov.br/).
- No campo **''Pesquisar''**, digite o nome do município desejado.
- Na página do município, localize o item **"Código do Município"**.
- Copie o código de **7 dígitos** informado.

**(4)** Retorne à tela "Cidades" (Configurações » Cadastros » Endereços) e insira o código correto no campo "Mun. domicílio fiscal".

**(5)** Salve as alterações.

**(6)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize os parceiros envolvidos no documento fiscal rejeitado (destinatário, remetente ou transportadora).

**(7)** Na aba **"Endereço"**, confirme se o campo **"Cód. Cidade"** está preenchido e vinculado ao cadastro da cidade correto, ajustado anteriormente.

**(8)** Se necessário, acesse a tela [**"Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) (Configurações » Cadastros » Empresas). Na aba **"Endereço"**, verifique se o campo **"Cidade"** está preenchido com um município que possua um **código IBGE válido**.

**(9)** Após realizar os ajustes nos cadastros, retorne ao documento fiscal rejeitado e redigite os dados do cabeçalho para que o sistema capture as informações atualizadas.

**(10)** Gere um novo lote de transmissão do documento fiscal.

**(10)** Se a rejeição persistir, inutilize ou exclua o documento rejeitado e refaça o lançamento completamente.

**OBSERVAÇÃO:** Caso não consiga localizar a informação do código do município no site do IBGE, solicite auxílio ao seu contador.

**CAUSA**

Esta rejeição ocorre quando o **código do município** informado no documento fiscal eletrônico está **ausente, incorreto ou não corresponde** a um código válido na tabela oficial de municípios do IBGE. O sistema da SEFAZ valida se o código possui **7 dígitos** e se está devidamente cadastrado na base de dados oficial. Quando o campo **"Mun. domicílio fiscal"** não está preenchido no cadastro de cidades, ou quando há divergência entre o código informado e a tabela do IBGE, o documento é rejeitado para garantir a **integridade e padronização** das informações fiscais.
