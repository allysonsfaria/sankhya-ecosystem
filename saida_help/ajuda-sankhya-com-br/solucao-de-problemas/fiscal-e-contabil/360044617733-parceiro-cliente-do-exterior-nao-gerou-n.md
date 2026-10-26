---
id: "360044617733"
titulo: "Parceiro/Cliente do Exterior, não gerou no registro 0150 do EFD-Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617733-Parceiro-Cliente-do-Exterior-n%C3%A3o-gerou-no-registro-0150-do-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:34Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Cadastro", "EFD Contribuições", "Informe o código 55 para \"CODPAISBRASIL\".", "Crie cadastro para o país e estado do exterior.", "Vincule a cidade cadastrada ao parceiro do exterior.", "País"]
---

# Parceiro/Cliente do Exterior, não gerou no registro 0150 do EFD-Contribuições

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16612047679767) MENSAGEM:**

Parceiro/Cliente do Exterior, não gerou no registro 0150 do EFD-Contribuições.

**![Imagem 2: SOLUÇÃO: Para correção deste erro, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16612040049687) SOLUÇÃO:**
Para correção deste erro, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências :](https://ajuda.sankhya.com.br/hc/article_attachments/16612040051991) Acesse: Configurações » Avançado » Preferências:

- **"CODPAISBRASIL-Código do País Brasil":** informe o valor: 55

![Imagem 4: "CODPAISBRASIL-Código do País Brasil": informe o valor: 55](https://ajuda.sankhya.com.br/hc/article_attachments/14919266212887)

![Imagem 5: Acesse: Configurações » Cadastros » Endereços » Países :](https://ajuda.sankhya.com.br/hc/article_attachments/16612047690135) Acesse: Configurações » Cadastros » Endereços » Países:

Crie o cadastro do Pais do Exterior. Lembrando de verificar junto ao [BACEN](http://www.bcb.gov.br/pt-br#!/home) o código do 'Pais Domicilio Fiscal

- Exemplo:
  Código do Brasil: 1058
  Código do México: 4936

![Imagem 6: Acesse: Configurações » Cadastros » Endereços » Estados :](https://ajuda.sankhya.com.br/hc/article_attachments/16612047694231) Acesse: Configurações » Cadastros » Endereços » Estados:

- Crie um Estado com as características abaixo:
  Descrição: EXTERIOR
  Pais: informe o cadastro feito no item 2
  Sigla: EX
  Código IBGE = 99

![Imagem 7: Acesse: Configurações » Cadastros » Endereços » Cidades:](https://ajuda.sankhya.com.br/hc/article_attachments/16612040061207) Acesse: Configurações » Cadastros » Endereços » Cidades:

- Crie uma Cidade com a descrição referente ao Endereço do Pais do Exterior
  Cód; UF: Informe o Estado criado no item 3
  Mun. domicílio fiscal= 9999999

![Imagem 8: Acesse: Configurações » Cadastros » Parceiros :](https://ajuda.sankhya.com.br/hc/article_attachments/16612040064791) Acesse: Configurações » Cadastros » Parceiros:

- Vincule a Cidade cadastrada no item 4 ao parceiro do Exterior
- Aba **"Endereço"**, campo » **"Cód. Cidade"**.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16612040068631)CAUSA:**

Ao gerar o EFD Contribuições o parceiro do Exterior não está no Registro 1050 devido a falta de configurações da Cidade do Exterior.
