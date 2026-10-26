---
id: "37226107617303"
titulo: "E0591 Rejeição: Não é permitido informar o código do país onde ocorreu o resultado do serviço prestado para os cenários diferentes de 2, 30, 58, 62, 72, 76 conforme a planilha \"EXPORTACAO_EMISSÃO_NFS-e\"."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226107617303-E0591-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-o-c%C3%B3digo-do-pa%C3%ADs-onde-ocorreu-o-resultado-do-servi%C3%A7o-prestado-para-os-cen%C3%A1rios-diferentes-de-2-30-58-62-72-76-conforme-a-planilha-EXPORTACAO-EMISS%C3%83O-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:18Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "TOP", "Financeiro", "NFS-e", "Código do País", "Planilha \"EXPORTACAO_EMISSÃO_NFS-e", "Código do país onde ocorreu o resultado do serviço", "Cenários de exportação"]
---

# E0591 Rejeição: Não é permitido informar o código do país onde ocorreu o resultado do serviço prestado para os cenários diferentes de 2, 30, 58, 62, 72, 76 conforme a planilha "EXPORTACAO_EMISSÃO_NFS-e".

**MENSAGEM**

E0591 Rejeição: Não é permitido informar o código do país onde ocorreu o resultado do serviço prestado para os cenários diferentes de 2, 30, 58, 62, 72, 76 conforme a planilha "EXPORTACAO\_EMISSÃO\_NFS-e".

**SITUAÇÃO**

Ao emitir uma NFS-e, o usuário informou o **código do país** onde ocorreu o resultado do serviço prestado, porém a **operação não se enquadra** nos cenários de exportação permitidos.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Tipo de Operações - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Identifique a TOP utilizada na emissão da nota fiscal que foi rejeitada.

**(3)** Na aba **"NFS-e"** valide se o campo **“Natureza Oper. ISS (NFS-e)”** está configurado corretamente:

- **Operação não é de exportação:** verifique se o **código do país** não está preenchido no documento fiscal.
- **Operação de exportação:** confirme se ela se enquadra em um dos cenários permitidos (**códigos 2, 30, 58, 62, 72 ou 76**).

**(4)** Caso a operação **não seja de exportação**, acesse o documento fiscal rejeitado e remova o **código do país** informado no campo correspondente.

**(5)** Se a operação **for de exportação**, mas não se enquadrar nos cenários permitidos, ajuste a **"Natureza Oper. ISS (NFS-e)"** na TOP para refletir corretamente o tipo de operação:

- **Código 1:** Exigível
- **Código 2:** Não incidência
- **Código 3:** Isenção
- **Código 4:** Exportação
- **Código 5:** Imunidade
- **Código 6:** Exigibilidade suspensa por decisão judicial
- **Código 7:** Exigibilidade suspensa por procedimento administrativo

**(6)** Após realizar todos os ajustes, emita novamente a NFS-e com as informações corretas.

**CAUSA**

A rejeição ocorreu porque o **código do país** foi informado em uma operação que **não se enquadra nos cenários de exportação** permitidos pela Sefaz. Segundo as regras de validação, o preenchimento do código do país onde ocorreu o resultado do serviço prestado é **obrigatório apenas para operações específicas de exportação**, identificadas pelos códigos 2, 30, 58, 62, 72 ou 76 na planilha "EXPORTACAO\_EMISSÃO\_NFS-e". Para operações que não se enquadram nesses cenários, o campo deve permanecer **vazio**.
