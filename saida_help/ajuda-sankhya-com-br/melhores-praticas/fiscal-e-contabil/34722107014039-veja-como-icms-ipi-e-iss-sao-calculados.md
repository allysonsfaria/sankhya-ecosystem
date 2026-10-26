---
id: "34722107014039"
titulo: "Veja como ICMS, IPI e ISS são calculados na Central quando a TOP está configurada como “Calcula na Confirmação”"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34722107014039-Veja-como-ICMS-IPI-e-ISS-s%C3%A3o-calculados-na-Central-quando-a-TOP-est%C3%A1-configurada-como-Calcula-na-Confirma%C3%A7%C3%A3o"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-09-03T14:47:32Z"
rotulos: ["ISS", "Configuração", "IPI", "ICMS", "Impostos", "TOP", "Central de vendas", "Central de compras", "TOP impostos", "Calcula na confirmação", "Calcular na confirmação", "Cálculo de ICMS IPI e ISS", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Central de Projetos"]
---

# Veja como ICMS, IPI e ISS são calculados na Central quando a TOP está configurada como “Calcula na Confirmação”

Quando a TOP está configurada com a opção **“Calcula na Confirmação”,** no campo **“Cálculo de ICMS, IPI e ISS”**, **nenhum imposto é exibido no momento do lançamento do item**. Isso significa que todos os tributos da nota, sejam eles ICMS, IPI, ISS ou quaisquer outros, somente serão calculados e apresentados na etapa de confirmação da nota.

Esse comportamento muda a experiência de conferência dos valores durante o lançamento, pois o sistema posterga o cálculo dos impostos. Assim, tanto os valores normalmente apresentados em **Outras Opções >> Outros Impostos**, quanto aqueles acessados em **Outras Opções >> Consultar/Alterar dados dos impostos do item**, não estarão disponíveis até que a nota seja confirmada.

Na prática, essa configuração é útil em cenários onde se deseja garantir que os impostos sejam calculados considerando todas as condições finais da nota (como descontos, rateios e tratamentos fiscais aplicados no fechamento). Por outro lado, é importante que o usuário esteja ciente de que, até a confirmação, **nenhuma informação de impostos estará acessível** para validação no lançamento do item.
