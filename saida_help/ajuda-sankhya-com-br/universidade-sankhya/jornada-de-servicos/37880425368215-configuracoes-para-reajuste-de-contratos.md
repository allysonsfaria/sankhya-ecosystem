---
id: "37880425368215"
titulo: "Configurações para reajuste de contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880425368215-Configura%C3%A7%C3%B5es-para-reajuste-de-contratos"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-22T14:06:35Z"
rotulos: ["Configuração", "Contrato", "Movimentação Financeira", "Preferências", "Financeiro"]
---

# Configurações para reajuste de contratos

1. **Verificação de parâmetros para reajuste**

- Acesse a tela **Preferências**
  Menu: Configurações  » Avançado
- Busque pelo parâmetro “**MOEREAJCON  - Uso de moeda em reajuste de contrato**” e no campo **Valor**, informe “Usar alternativa quando moeda principal negativa”.
- Busque também o parâmetro **“NOVOREAJCONT - Permite novo reajuste de contrato?”** e marque como **ligado**. Este parâmetro define quando o sistema considera o contrato apto para reajuste com base na data base e na frequência, estando ligado o sistema utiliza a seguinte fórmula de cálculo:  **Data base reajuste + (Frequência reajuste - 1) <= Último dia do mês atual,** desligado, o sistema permite o reajuste 2 meses antes do mês de faturamento, utilizando a fórmula: **Data base reajuste + (Frequência reajuste - 2) <= Último dia do mês atual.**
- Localize o parâmetro **“REAJAPARTDTBASE - Reajustar contrato a partir da data de reajuste?”** deixe-o **desligado**,  este parâmetro define qual período de índices o sistema vai considerar para calcular o reajuste do contrato. Os índices econômicos (como o IGPM ou IPCA) são divulgados no fim de cada mês, e isso influencia se o reajuste pode ser feito antes ou depois da data base. 
  **Ativado**: considera os índices a partir da data base. Só permite reajuste se já estiver no mês da data base, utilizando a fórmula: **data base do reajuste + frequência - 1.**

**Desativado**: considera os índices até o mês anterior à data base. Permite reajuste antecipado, logo no início do mês utilizando a fórmula: **-1 mês até a data base do reajuste + frequência - 1.**

**Importante:** A escolha entre ativar ou desativar esse parâmetro depende do processo adotado pela empresa. Se o reajuste precisa acontecer logo no início do mês, é recomendado manter o parâmetro desativado. Se o processo exige que a data base já tenha sido atingida e que se aguarde a liberação dos índices mais recentes, então o parâmetro deve ser ativado.
