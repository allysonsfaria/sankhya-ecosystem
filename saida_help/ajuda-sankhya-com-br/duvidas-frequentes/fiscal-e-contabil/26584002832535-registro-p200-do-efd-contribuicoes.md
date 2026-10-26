---
id: "26584002832535"
titulo: "Registro P200 do EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26584002832535-Registro-P200-do-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:41:09Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "EFD Contribuições", "Registro P200 do EFD Contribuições", "P200"]
---

# Registro P200 do EFD Contribuições

Confira as regras e condições para geração do registro P200, do EFD Contribuições, em nossa solução ERP.

### Conceito (Guia Prático)

Registro de consolidação da contribuição previdenciária incidente sobre o valor da receita bruta, devida pela empresa no período correspondente ao somatório da contribuição sobre a receita bruta mensal de cada estabelecimento, apurada no Registro “P100”.

Em nossa aplicação, existem algumas regras para que o registro seja executado na geração do TXT:

![Imagem 1: Deve ter sido gerado algum P100 ( Registro P100 do EFD Contribuições );](https://ajuda.sankhya.com.br/hc/article_attachments/26652218903575)  Deve ter sido gerado algum P100 ([Registro P100 do EFD Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/26555446175639-Registro-P100-do-EFD-Contribui%C3%A7%C3%B5es));

![Imagem 2: Na tela "Empresa" (Caminho: Comercial » Preferências » Empresa) , aba "EFD - Escrituração Fiscal Digital" , posicionado…](https://ajuda.sankhya.com.br/hc/article_attachments/26652218907159)  Na tela **"Empresa"** (Caminho: Comercial » Preferências » Empresa), aba **"EFD - Escrituração Fiscal Digital"**, posicionado na seção **"EFD Contribuições"**, marque o registro **"P200"** para gerar;

Como já mencionado, sua geração será sobre os valores processados no P100, o que vale ressaltar os seguintes campos do registro P200:

(1)** Campo PER\_REF:** será a data inicial de geração do TXT;

(1)** Campo COD\_REC:** se nos Produtos que foram considerados na geração do P100, houver código [**"Cód. Atividade CPRB (Reintegra/Prev.)"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608314-C%C3%B3d-Atividades-Produtos-e-Servi%C3%A7os-p-CPRB) preenchido, o sistema usará o valor informado neste código, no campo **"Código de Recolhimento".** Caso o referido campo não contenha informações, será buscado nas Preferências da Empresa, aba **"Reintegra Previdência"**, campo **"Código de Recolhimento"**.

**(1)** **Campo VL\_TOT\_CONT\_APU:** valor total apurado da Contribuição Previdenciária sobre a Receita Bruta (Somatório do Campo 10 “VL\_CONT\_APU“, do(s) Registro(s) P100);

Atualmente existem alguns campos para os quais nossa aplicação não realiza o processamento:

VL\_TOT\_AJ\_REDUC

VL\_TOT\_AJ\_ACRES
