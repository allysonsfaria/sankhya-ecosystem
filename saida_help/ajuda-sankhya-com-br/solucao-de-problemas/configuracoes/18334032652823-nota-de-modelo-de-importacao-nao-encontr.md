---
id: "18334032652823"
titulo: "Nota de modelo de importação não encontrada no sistema: 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18334032652823-Nota-de-modelo-de-importa%C3%A7%C3%A3o-n%C3%A3o-encontrada-no-sistema-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-15T21:08:35Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "XML", "Importação", "CFOP", "Nota de Importação Ausente"]
---

# Nota de modelo de importação não encontrada no sistema: 'X'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18334032642455) **MENSAGEM:**

Nota de modelo de importação não encontrada no sistema: 'X'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18334012543383)CAUSA:**

Ocorre quando o modelo vinculado a um destes cenários citados acima não existe no sistema.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18334043022487)SOLUÇÃO:**

![Imagem 4: Será verificado se o parceiro fornecedor do XML é produtor rural; se for, será utilizado o modelo de importação…](https://ajuda.sankhya.com.br/hc/article_attachments/18341954512407) Será verificado se o parceiro fornecedor do XML é produtor rural; se for, será utilizado o modelo de importação definido para esses fornecedores (Portal de importação de XML, botão Outras Opções, Preferências para importação de NF-e, campo Modelo de importação para Produtor Rural), se não;

![Imagem 5: O sistema analisa se o parceiro fornecedor do XML possui algum modelo de importação determinado como fixo (Cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/18341961337751) O sistema analisa se o parceiro fornecedor do XML possui algum modelo de importação determinado como fixo (Cadastro de Parceiros, aba Fiscal, campo Modelo para Importação de XML Compra); se possuir, este modelo será utilizado, se não;

![Imagem 6: Será verificado se existe alguma combinação de CFOP(s) com o(s) CFOP(s) do XML (Portal de importação de XML, botão…](https://ajuda.sankhya.com.br/hc/article_attachments/18341954538007) Será verificado se existe alguma combinação de CFOP(s) com o(s) CFOP(s) do XML (Portal de importação de XML, botão Outras Opções, Configuração de Modelo p/ Compra por CFOP); se existir, o modelo de importação encontrado na combinação será utilizado, se não;

![Imagem 7: O sistema irá verificar se o XML possui o campo xPed preenchido para obtenção do Tipo de Operação; se houver, essa…](https://ajuda.sankhya.com.br/hc/article_attachments/18341954544919) O sistema irá verificar se o XML possui o campo xPed preenchido para obtenção do Tipo de Operação; se houver, essa busca será feita, se não;

![Imagem 8: Por fim, o sistema irá verificar se existe modelo de importação de XML nas Preferências da Empresa destinatária da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/18341954550935) Por fim, o sistema irá verificar se existe modelo de importação de XML nas Preferências da Empresa destinatária da nota importada.

**Atenção:** Valide todas as informações acima utilizando o usuário SUP.
