---
id: "44012734879511"
titulo: "[TMS] - Como Funciona o Cálculo e Rateio do ICMS e ISS em Embarques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012734879511--TMS-Como-Funciona-o-C%C3%A1lculo-e-Rateio-do-ICMS-e-ISS-em-Embarques"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:38:11Z"
rotulos: ["sync_hc", "lincros", "sync_hash_04c5c0af4667", "lincros_13433253"]
---

# [TMS] - Como Funciona o Cálculo e Rateio do ICMS e ISS em Embarques

**1 - Problema Relatado pelo Cliente:**
O cliente busca compreender de forma clara como funciona o cálculo e o rateio do ICMS (Imposto sobre Circulação de Mercadorias e Serviços) e do ISS (Imposto sobre Serviços) dentro de um embarque, especialmente em relação ao comportamento do sistema com o parâmetro **calcularICMSISSEmbarqueDestinoConhecimento** ativado ou desativado. O objetivo é esclarecer a lógica que o sistema utiliza para consolidar e ratear a base de cálculo do ICMS e do ISS entre os documentos de um embarque, evitando dúvidas e interpretações incorretas sobre os valores gerados.

---

**2 - Passo a Passo para Resolver o Problema:**

A seguir, apresentamos a explicação detalhada do comportamento do sistema para o cálculo e rateio do ICMS e ISS no embarque, conforme o status do parâmetro **calcularICMSISSEmbarqueDestinoConhecimento**:

## Quando o parâmetro está ATIVO:

- O sistema irá agrupar todas as notas fiscais dentro do embarque que possuam o **mesmo destinatário** (mesmo destino).
- Em seguida, o sistema somará as bases de cálculo dessas notas fiscais que possuem o mesmo destinatário.
- O ISS ou ICMS será calculado sobre essa base somada e, posteriormente, o sistema realizará o rateio proporcional do imposto entre as notas fiscais agrupadas com o mesmo destinatário.
- Ou seja, para cada grupo de notas com o mesmo destinatário, será realizado um cálculo único de base, seguido do rateio proporcional do ISS/ICMS.

**Exemplo prático:**

- Em um embarque com 12 documentos, sendo 6 deles destinados a um mesmo cliente:

  - O sistema agrupa essas 6 notas;
  - Calcula a base total do ICMS/ISS considerando a soma dessas notas;
  - Realiza o rateio proporcional do ICMS/ISS entre esses 6 documentos.
- As demais notas do embarque, que são para destinatários distintos, terão o cálculo do ICMS/ISS feito de forma isolada, uma vez que não há agrupamento.

---

## Quando o parâmetro está INATIVO:

- O sistema desconsidera as origens e destinos individuais de cada nota fiscal e pré-conhecimento.
- O cálculo do ISS ou ICMS será feito considerando **exclusivamente a origem e destino do embarque** como um todo.
- Assim, a base de cálculo do imposto será formada com a **soma de todas as notas fiscais do embarque**, independentemente de suas origens ou destinatários.
- O sistema, então, rateará o ICMS/ISS proporcionalmente entre todos os documentos do embarque, sem distinção por destinatário.
- Exemplo: se a origem e destino do embarque incide o ICMS, então este será o imposto calculado sobre a base de cálculo de todas as notas fiscais do embarque, mesmo que haja nota fiscal que, originalmente, incide ISS.

---

## Outros pontos importantes sobre o cálculo:

- O sistema sempre realiza o cálculo utilizando **quatro casas decimais**, garantindo maior precisão no valor do imposto rateado.
- O comportamento descrito acima está implementado de forma consistente e não sofre alterações fora da ativação ou desativação do parâmetro mencionado.
- O tipo de distribuição do rateio depende da configuração de parâmetro que determina se o rateio será por valor da nota fiscal, peso, cubagem etc.
