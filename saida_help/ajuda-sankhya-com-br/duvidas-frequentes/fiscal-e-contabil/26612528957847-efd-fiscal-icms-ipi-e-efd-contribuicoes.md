---
id: "26612528957847"
titulo: "EFD FISCAL ICMS/IPI e EFD Contribuições - Parâmetro CONSCABLIVEFD - Campo 12 C100"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26612528957847-EFD-FISCAL-ICMS-IPI-e-EFD-Contribui%C3%A7%C3%B5es-Par%C3%A2metro-CONSCABLIVEFD-Campo-12-C100"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-18T17:23:00Z"
rotulos: ["Configuração", "IPI", "ICMS", "Impostos", "CONSIMPRETNOTA", "EFD", "EFD Contribuições", "CONSCABLIVEFD", "Campo 10 C100", "TGFCAB.HISTCONFIG", "INSS é retido?", "ISS Retido na fonte", "Vlr. do IRF"]
---

# EFD FISCAL ICMS/IPI e EFD Contribuições - Parâmetro CONSCABLIVEFD - Campo 12 C100

Existe a possibilidade de gerar no registro C100, campo 12 VL\_DOC de forma a ficar líquido de impostos retidos na nota ou bruto desses valores, seguindo as seguintes regras:

Se o parâmetro **CONSCABLIVEFD** estiver desligado, o campo **TGFCAB.HISTCONFIG** estiver **vazio** e o parâmetro **CONSIMPRETNOTA** estiver ligado, o sistema vai calcular o campo "Valor total do documento fiscal" (VL\_DOC - C100) líquido dos impostos retidos em "outros impostos" dos itens, também dos valores de INSS e ISS se, no cabeçalho da nota, os campos:

- **"INSS é retido?"** e **"ISS Retido na fonte"** estiverem marcados respectivamente.

Mesmo que o parâmetro CONSIMPRETNOTA esteja desligado, será deduzido o valor do campo **"Vlr. do IRF"**.

Caso o referido parâmetro CONSCABLIVEFD esteja ligado, o valor do campo citado será apresentado bruto dos impostos citados.
