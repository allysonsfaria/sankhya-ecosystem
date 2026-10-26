---
id: "43941266613911"
titulo: "Processo Adequação da NF-e à NT 2026.007 · v1.00 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43941266613911-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-007-v1-00-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2026.007 · v1.00 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/43948501784855)

## NT 2026.007 v1.00 – Emissão de NF-e por contribuinte exclusivo do IBS/CBS (sem Inscrição Estadual)

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 07/2026. Contribuintes do IBS/CBS que não são contribuintes do ICMS passam a emitir NF-e sem Inscrição Estadual (IE), com autorização centralizada na SVRS. A NT também cria validações cadastrais na Lista Centralizada de Contribuintes da RFB (LCC-RFB) e no CCC.

### Prazos

- **Homologação (teste): desde 01/09/2026.** Novo campo C17 opcional e regras de validação disponíveis no ambiente de teste.
- **Produção: 03/11/2026.** Emissão sem IE e validações na LCC-RFB e no CCC passam a valer para todos os emissores.

### O que muda na v1.00

#### 1. emit/IE – Emitente sem IE: contribuinte exclusivo do IBS/CBS (Rejeições 163 e 164)

O campo C17 passa a ter ocorrência 0-1. É contribuinte exclusivo o emitente que, ao mesmo tempo:

- Não informa a tag emit/IE.
- Tem CNPJ com situação Ativa na Receita Federal.
- Não possui IE habilitada para ICMS na UF, conforme o CCC.

A regra C17-10 (IE não informada) foi excluída. IE preenchida com zeros continua rejeitada pela C17-20.

#### 2. SVRS – Autorização centralizada e restrições (Rejeições 166, 156 a 158 e 188)

A NF-e sem IE é autorizada somente na SVRS, e as regras de UF do emitente e da chave de acesso (B02-10, C12-10, P12-40) ganham exceção para esse caso.

- Proibido emitir NFC-e sem IE até 2033.
- CNPJ do emitente obrigatório e IEST proibida.
- Eventos de autoria do emitente sem IE também vão para a SVRS.

#### 3. N01-10, UB12-11 e I08-191 – Tributos e CFOP sem IE (Rejeições 161, 162 e 159)

Na NF-e sem IE, é proibido informar ICMS e ICMSUFDest, o grupo IBSCBS é obrigatório e o CFOP deve estar na tabela de CFOP permitidos (coluna indExcIBSCBS). A B25-90 deixa de exigir ICMS ou ISSQN nesse cenário.

Devolução (finNFe = 4) e tpNFCredito = 03 ficam fora das regras de ICMS e CFOP.

#### 4. LCC-RFB e CCC – Validações cadastrais na Receita e no CCC (Rejeições 178 a 187, 180 e 165 a 177)

Emitente, destinatário, locais de retirada e entrega e autor de evento passam a ser verificados na LCC-RFB: CNPJ não cadastrado ou com situação diferente de 02-Ativa gera rejeição.

O CRT da nota deve ser compatível com o regime tributário da LCC-RFB, e IE e CNPJ dos locais de retirada e entrega são conferidos no CCC. A regra 5E17-70 foi excluída, substituída pelas regras da LCC-RFB.

### Calendário

- **07/2026 (publicação, v1.00):** publicação da NT no Portal Nacional da NF-e.
- **01/09/2026 (homologação, v1.00):** emissão sem IE, autorização na SVRS e validações na LCC-RFB e no CCC.
- **03/11/2026 (produção, v1.00):** todas as regras da NT valendo para os emissores.

Fonte: NT 2026.007 v1.00 – Portal Nacional da NF-e, publicada em 07/2026.
