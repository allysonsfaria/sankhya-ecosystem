---
id: "37224883601559"
titulo: "E0382 Rejeição: O CEP não deve ser informado quando o endereço da obra ocorrer no exterior do país."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224883601559-E0382-Rejei%C3%A7%C3%A3o-O-CEP-n%C3%A3o-deve-ser-informado-quando-o-endere%C3%A7o-da-obra-ocorrer-no-exterior-do-pa%C3%ADs"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:23Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SEFAZ", "CEP", "Erro", "NF-e ou NFC-e", "CEP não deve ser informado", "Endereço da obra está cadastrado com um país estrangeiro", "País", "Cadastro de País estrangeiro", "Obra no exterior do país", "Documentos Eletrônicos"]
---

# E0382 Rejeição: O CEP não deve ser informado quando o endereço da obra ocorrer no exterior do país.

**MENSAGEM**

E0382 Rejeição: O CEP não deve ser informado quando o endereço da obra ocorrer no exterior do país.

**SITUAÇÃO**

Ao tentar emitir uma **NF-e ou NFC-e** vinculada a uma obra localizada no exterior, o sistema apresenta a rejeição E0382. Isso ocorre quando o **endereço da obra está cadastrado com um país estrangeiro**, mas o campo **"CEP"** permanece preenchido no cadastro.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Obras"** (INSERIR CAMINHO DA TELA) e localize o cadastro da obra vinculada à nota fiscal que está sendo emitida.

**(2)** Na aba **"Endereço"**, verifique se o campo **"País"** está preenchido com um país diferente do Brasil.

**(3)** Caso o país seja do exterior, **remova o conteúdo do campo "CEP"**, deixando-o em branco.

- Para obras no exterior, utilize apenas o campo **"Código Postal"** para informar o código postal do país correspondente.

**(4)** Certifique-se de que o campo **"UF"** esteja preenchido com **"EX"** (Exterior) e que a cidade esteja vinculada ao estado **"EXTERIOR"**.

**(5)** Salve as alterações no cadastro da obra.

**(6)** Retorne à nota fiscal e **gere um novo lote** para transmissão. 

**CAUSA**

A rejeição ocorre porque a **Sefaz não permite que o campo "CEP" seja informado** quando o endereço da obra está localizado no exterior do país. Para obras internacionais, apenas o **"Código Postal"** do país correspondente deve ser utilizado, mantendo o campo **"CEP"** vazio. A validação garante que os dados de endereçamento estejam corretos conforme a localização geográfica da obra.
