---
id: "37226118885271"
titulo: "E0590 Rejeição: É obrigatório informar o código do país onde ocorreu o resultado do serviço prestado para os cenários 2, 30, 58, 62, 72, 76, conforme a planilha \"EXPORTACAO_EMISSÃO_NFS-e\"."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226118885271-E0590-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-o-c%C3%B3digo-do-pa%C3%ADs-onde-ocorreu-o-resultado-do-servi%C3%A7o-prestado-para-os-cen%C3%A1rios-2-30-58-62-72-76-conforme-a-planilha-EXPORTACAO-EMISS%C3%83O-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:19Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "TOP", "NFS-e", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "Exportação de serviços", "Código do País", "Identificação do país do serviço prestado", "Operações de exportação de serviços", "Exportacao"]
---

# E0590 Rejeição: É obrigatório informar o código do país onde ocorreu o resultado do serviço prestado para os cenários 2, 30, 58, 62, 72, 76, conforme a planilha "EXPORTACAO_EMISSÃO_NFS-e".

**MENSAGEM**

E0590 Rejeição: É obrigatório informar o código do país onde ocorreu o resultado do serviço prestado para os cenários 2, 30, 58, 62, 72, 76, conforme a planilha "EXPORTACAO\_EMISSÃO\_NFS-e".

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** para operações de **exportação de serviços**, o usuário não informou o **código do país** onde ocorreu o resultado do serviço prestado. Esta informação é **obrigatória** para cenários específicos de exportação (códigos 2, 30, 58, 62, 72 e 76), conforme estabelecido pela planilha de exportação da Sefaz, resultando na rejeição do documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipo de Operações - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP utilizada na emissão da NFS-e.

**(2)** Acesse a aba **"NFS-e"**, verifique se o campo **"Natureza Oper. ISS (NFS-e)"** está selecionada a opção **"4 - Exportação"**.

**(3)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço.

**(4)** Na aba **"Endereço"**, verifique se o campo **"País"** está preenchido corretamente com o código do país onde o serviço foi prestado ou onde ocorreu o resultado do serviço.

- Utilize o **código numérico do país** conforme tabela de países da Receita Federal.
- Para operações de exportação nos cenários 2, 30, 58, 62, 72 e 76, este campo é **obrigatório**.

**(5)** Salve as alterações realizadas no cadastro do parceiro.

**(6)** Retorne à tela de emissão da NFS-e e emita novamente o documento fiscal com as informações corretas.

**CAUSA**

A rejeição ocorre porque, para **operações de exportação de serviços** enquadradas nos cenários específicos (2, 30, 58, 62, 72 e 76), a legislação fiscal exige a **identificação do país** onde o serviço foi prestado ou onde ocorreu o resultado do serviço.

A ausência desta informação no cadastro do tomador ou na configuração da operação impede que a Sefaz valide corretamente a natureza da operação de exportação, resultando na rejeição do documento fiscal eletrônico.
