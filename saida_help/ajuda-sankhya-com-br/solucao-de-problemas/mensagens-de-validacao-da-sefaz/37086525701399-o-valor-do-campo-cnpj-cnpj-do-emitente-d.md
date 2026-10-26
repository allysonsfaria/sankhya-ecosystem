---
id: "37086525701399"
titulo: "O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é valido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37086525701399-O-valor-do-campo-CNPJ-CNPJ-do-emitente-do-documento-fiscal-referenciado-informado-n%C3%A3o-%C3%A9-valido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:21:52Z"
rotulos: ["CORE_E04895", "CNPJ", "Fiscal", "NF-e", "SEFAZ", "Erro", "CNPJ do emitente", "Emitir documento fiscal", "Valor do campo CNPJ", "Documentos Eletrônicos"]
---

# O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é valido.

**MENSAGEM:**

“Erro
O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é valido.
Código: CORE\_E04895.”

**SITUAÇÃO**:

Ao tentar emitir ou confirmar um documento fiscal, o sistema apresenta a mensagem acima.

Esse erro indica que o CNPJ informado no documento fiscal referenciado não atende às validações exigidas pela SEFAZ.

##### SOLUÇÃO:

Siga os passos abaixo para correção:

(1)** Verifique o CNPJ do emitente**

- Confirme se o CNPJ informado no documento fiscal referenciado está correto.
- Utilize apenas números, sem pontos, barras ou traços.

(2)** Valide o cadastro da empresa**

- Acesse o cadastro da empresa no sistema.
- Certifique-se de que o CNPJ está correto e ativo.

(3)** Revise o documento fiscal referenciado**

Confira:

- Chave de acesso.
- CNPJ do emitente.
- Modelo e série da nota.

Se necessário, refaça o vínculo do documento referenciado.

(4)** Verifique o ambiente de emissão**

- Confirme se a nota referenciada pertence ao mesmo ambiente (Produção ou Homologação).

#####

##### CAUSA:

A inconsistência ocorre devido a divergências nos dados do documento fiscal referenciado, geralmente relacionadas a:

- CNPJ inválido, incorreto ou incompleto.
- CNPJ com dígito verificador inválido ou com caracteres indevidos.
- CNPJ diferente do cadastrado para a empresa emissora.
- Documento fiscal referenciado cadastrado incorretamente.
- Nota fiscal referenciada com dados divergentes (modelo, série ou chave de acesso).
- Chave de acesso informada manualmente com erro.
- Utilização de ambiente incorreto (Produção x Homologação), como referência a uma nota de homologação em ambiente de produção ou vice-versa.
