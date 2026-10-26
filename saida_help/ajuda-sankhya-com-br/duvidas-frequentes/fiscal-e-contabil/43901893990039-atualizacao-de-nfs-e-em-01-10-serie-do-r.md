---
id: "43901893990039"
titulo: "Atualização de NFS-e em 01/10: série do RPS, código de serviço e NBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43901893990039-Atualiza%C3%A7%C3%A3o-de-NFS-e-em-01-10-s%C3%A9rie-do-RPS-c%C3%B3digo-de-servi%C3%A7o-e-NBS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-10-01T12:38:43Z"
---

# Atualização de NFS-e em 01/10: série do RPS, código de serviço e NBS

**Ação necessária:** em 01/10, as prefeituras de Campinas, Campo Grande, João Pessoa, Sorocaba e Teresina atualizam o sistema de emissão de NFS-e.

Para continuar emitindo notas fiscais de serviço sem rejeição, revise três configurações no Sankhya.

### Municípios afetados

- **São Paulo:** Campinas e Sorocaba. [Ver especificações de São Paulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/22511770305303-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-S%C3%A3o-Paulo)
- **Mato Grosso do Sul:** Campo Grande. [Ver especificações de Mato Grosso do Sul](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599828778263-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Mato-Grosso-do-Sul)
- **Paraíba:** João Pessoa. [Ver especificações da Paraíba](https://ajuda.sankhya.com.br/hc/pt-br/articles/22592883989783-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Para%C3%ADba)
- **Piauí:** Teresina. [Ver especificações do Piauí](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD)

### 1. Ajuste a série do RPS

Após a atualização, a prefeitura aceita apenas séries entre **10001** e **49999**. A série enviada é formada pelo prefixo da empresa seguido da série da TOP.

- **Prefixo:** em Preferências da Empresa > Documentos Fiscais Eletrônicos > NFS-e > Geral, preencha o campo **Prefixo Série NFS-e Padrão Nacional** com 2 dígitos. Exemplo: 10.
- **Série:** em Tipos de Operação (TOP), preencha o campo **Série** com o sequencial desejado, com 3 dígitos. Exemplo: 001.
- **Série enviada à prefeitura:** 10001, dentro do intervalo exigido.
- **Saiba mais:** [Especificações sobre a emissão de NFS-e no padrão nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional)

### 2. Informe o código de serviço com 9 dígitos

O código de serviço passa a ter obrigatoriamente 9 dígitos: 6 do código de serviço nacional e 3 do código de serviço municipal. Consulte o código municipal no portal da sua prefeitura.

| Código | Valor |
| --- | --- |
| Código de serviço nacional | 160201 |
| Código de serviço municipal | 005 |
| **Código de serviço completo** | **160201005** |

**Saiba mais:** [Nota Fiscal Eletrônica de Serviço – Prefeituras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras) e as especificações do seu estado, na lista acima.

### 3. Ative o envio do código NBS

O código NBS (Nomenclatura Brasileira de Serviços) passa a ser obrigatório na emissão da NFS-e.

- **O que fazer:** no Cadastro de Cidades, aba NFS-e, ative a opção **Enviar o Código NBS no JSON**.
- **Confira também:** o campo **Código NBS** precisa estar preenchido no Cadastro de Serviços, aba Impostos.
- **Saiba mais:** [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) e [E0316 Rejeição: Código da lista NBS informado inexistente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224408355991-E0316-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-lista-NBS-informado-inexistente-tabela-de-NBS-do-sistema)

### Quando fazer os ajustes

Recomendamos revisar e ajustar os cadastros em 01/10, antes de emitir as primeiras notas do dia.

Se precisar de ajuda, fale com nossa equipe de suporte.
