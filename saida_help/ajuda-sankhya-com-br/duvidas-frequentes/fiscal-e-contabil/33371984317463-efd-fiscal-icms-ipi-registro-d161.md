---
id: "33371984317463"
titulo: "EFD FISCAL (ICMS/IPI) | Registro D161"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33371984317463-EFD-FISCAL-ICMS-IPI-Registro-D161"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:29:06Z"
rotulos: ["Configuração", "XML", "Escrituração Fiscal Digital", "EFD", "ICMS/IPI", "EFD FISCAL (ICMS/IPI)", "Registro D161", "Coleta", "Bloco D", "Rodapé", "Documentos Eletrônicos"]
---

# EFD FISCAL (ICMS/IPI) | Registro D161

Atualmente a aplicação está preparada para **gerar o registro D161**. Confira a seguir as regras de negócio do sistema para a execução desse processo:

**Atenção:** a chamada da geração desse registro ocorre durante a geração do registro D160, ou seja, ele é dependente da geração deste.

**(1)** Na tela **''Empresa''** (Comercial» Preferências» Empresa) na aba **"EFD - Escrituração Fiscal Digital"**, o **Bloco D** e o **registro D161** devem estar selecionados para a geração.

**(2)** No '**'Rodapé'**' das centrais, temos a aba **"Coleta"** (Tabela do banco de dados TGFNCE) onde informamos os dados de Coleta e Entrega, e onde o sistema busca as informações para serem populadas no registro D161:

![Imagem 1: (2) No ' 'Rodapé' ' das centrais, temos a aba "Coleta" (Tabela do banco de dados TGFNCE) onde informamos os dados de…](https://ajuda.sankhya.com.br/hc/article_attachments/33371984317079)

**(1)** Os campos do registro, são gerados pelo retorno da grade citada acima:

(2)**IND\_CARGA**: O que for definido no campo **"Tipo Transporte"**;

(2)**CNPJ\_CPF\_COL**: será preenchido quando o campo **"Tipo"** for **''Coleta''**. Se for preenchido manualmente, o campo **"CNPJ/CPF**", será levada essa informação para o campo no registro, porém, se for informado **"Cód. Parceiro"**, o sistema vai pegar a informação dele.

(2)**IE\_COL**: será preenchido quando o campo Tipo for Coleta. Se for preenchido manualmente, o campo **"Insc. Estadual"**, será levada essa informação para o campo no registro, porém, se for informado  Cód. Parceiro, o sistema vai pegar a informação dele.

(2)**COD\_MUN\_COL**: será preenchido quando o campo Tipo for Coleta. Se for preenchido manualmente, o campo **"Mun. domicílio fiscal"**, será levada essa informação para o campo no registro, porém, se for informado Cód. Parceiro, o sistema vai pegar a informação dele.

(2)**CNPJ\_CPF\_ENTG**: será preenchido quando o campo Tipo for Entrega. Se for preenchido manualmente, o campo CNPJ/CPF, será levada essa informação para o campo no registro, porém, se for informado Cód. Parceiro, o sistema vai pegar a informação dele.

(2)**IE\_ENTG**: será preenchido quando o campo Tipo for Entrega. Se for preenchido manualmente, o campo Insc. Estadual, será levada essa informação para o campo no registro, porém, se for informado Cód. Parceiro, o sistema vai pegar a informação dele.

(2)**COD\_MUN\_ENTG**: será preenchido quando o campo Tipo for Entrega. Se for preenchido manualmente, o campo Mun. domicílio fiscal, será levada essa informação para o campo no registro, porém, se for informado Cód. Parceiro, o sistema vai pegar a informação dele.
