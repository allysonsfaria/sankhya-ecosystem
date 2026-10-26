---
id: "34637493829399"
titulo: "Melhores Práticas para Apuração de PIS e COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34637493829399-Melhores-Pr%C3%A1ticas-para-Apura%C3%A7%C3%A3o-de-PIS-e-COFINS"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:26:55Z"
rotulos: ["Configuração", "Relatórios", "COFINS", "PIS", "Impostos", "Financeiro", "EFD Contribuições", "Apuração de PIS e COFINS", "validador do PVA", "Painel de Auditoria de PIS e COFINS", "Relatório de Conferência de PIS e COFINS", "Melhores Práticas para Apuração de PIS e COFINS", "Programa Validador e Assinador do SPED", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Melhores Práticas para Apuração de PIS e COFINS

O Sankhya não realiza a apuração de PIS e COFINS. A responsabilidade de calcular e validar esses tributos é **"do validador do PVA (Programa Validador e Assinador do SPED)"**.

Isso significa que, **ao importar os dados para o PVA, o validador será o responsável por:**

- Identificar notas fiscais de entrada e saída;
- Criar o **"Bloco M"** de PIS e COFINS;
- Aplicar as regras de tributação conforme o Guia Prático da Receita Federal.

**É importante reforçar** que o **Sankhya apenas disponibiliza os dados para conferência, não substitui a apuração oficial no PVA.**

![Imagem 1: É importante reforçar que o Sankhya apenas disponibiliza os dados para conferência, não substitui a apuração oficial no…](https://ajuda.sankhya.com.br/hc/article_attachments/34637493825815)

A Conferência de PIS e COFINS trata-se de um dashboard que apresenta todas as notas contidas no livro de ICMS e no livro de ISS de cada cliente, a fim se confirmar se todas estão com a tributação de PIS e COFINS correta.

Esse dashboard contém seis opções de consultas, de forma que tragam todas as movimentações de Entradas e Saídas que estejam escrituradas nos Livros de ICMS/IPI e ISS, bem como as Depreciações e as Aquisições de Ativos Imobilizados.

independente de CFOP e de Operações que tenham tributação ou não de PIS/COFINS, de forma que seja possível conferir todos os documentos antes da apuração destes impostos.

Ou seja, ele não valida as regras do guia prático. É para simples conferência do que teve ou não cálculo de PIS e COFIN na TGFDIN.

[Saiba mais sobre o Painel de Auditoria](https://ajuda.sankhya.com.br/hc/pt-br/articles/10135864060183-Painel-de-Auditoria-de-PIS-COFINS?utm_source=chatgpt.com)

Ao utilizar o **"Painel de Auditoria"**, podem ocorrer divergências específicas. Abaixo, apresentamos as soluções para os cenários mais comuns:

**Cenário 1 - Aquisições de imobilizado (base de cálculo sem dedução de ICMS):**

O código SQL do relatório pode calcular a base de PIS/COFINS apenas dividindo o valor de aquisição, sem considerar a exclusão do ICMS. Para corrigir:

Acesse a tela **"Empresa Financeiro"** (Configurações >> Cadastros >> Empresas).

Localize o parâmetro **"Deduzir valor de ICMS próprio da compra da BC do PIS e COFINS da Venda? - DEDICMSBCPISCOFINS"**.

Configure como **"S"**.

Salve e recalcule as notas de imobilizado afetadas.

**Cenário 2 - Alíquotas incorretas em entradas financeiras:**

Se o sistema apresenta alíquotas incorretas, pode ser necessária uma correção técnica na consulta SQL, garantindo a inclusão do filtro **"TGFIIF.TIPBASE = 'V'"**. Caso o problema persista, abra um chamado técnico relatando que a consulta não filtra corretamente o campo TGFIIF.TIPBASE.

**Cenário 3 - Natureza da base de cálculo (configuração no tipo de operação):**

Para CT-es, certifique-se de que o campo **"Natureza da Base de Cálculo do Crédito de Pis/Cofins" (NATBCCRED)** esteja preenchido adequadamente no cadastro do **"Tipo de Operação"** (Configurações >> Cadastros >> Tipos de Operação - TOP) utilizado. As principais naturezas incluem: 01 (Aquisição de bens para revenda), 05 (Aluguéis de prédios), 06 (Aluguéis de máquinas e equipamentos) e 18 (Estoque de abertura de bens).

### Relatório de conferência de PIS e COFINS

O **"Relatório de Conferência"** (Comercial >> Relatórios >> Relatório de Conferência PIS/COFINS) oferece uma visão parcial das informações que irão compor a apuração no PVA:

- Serve para **"simples conferência"**;
- Ajuda a verificar consistência e identificar divergências;
- Não deve ser considerado como apuração final ou substitutivo do PVA.

[Saiba mais sobre o Relatório de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS?utm_source=chatgpt.com)

### Melhores práticas

**Sempre valide no PVA**: Utilize o Sankhya apenas como conferência, mas a apuração oficial deve ser feita no PVA;

**Revise notas de entrada, saída e CT-es**: Antes de importar, verifique se todas as notas e conhecimentos estão corretos e classificados;

**Utilize os relatórios e painéis para auditoria**: Identifique inconsistências e corrija antes da importação;

**Treinamento e atualização**: Mantenha a equipe atualizada sobre o Guia Prático de PIS/COFINS e sobre as funcionalidades do Sankhya.
