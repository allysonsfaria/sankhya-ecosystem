---
id: "39334356994455"
titulo: "Como configurar CBS e IBS com base de cálculo reduzida no ERP Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39334356994455-Como-configurar-CBS-e-IBS-com-base-de-c%C3%A1lculo-reduzida-no-ERP-Sankhya"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-13T16:08:09Z"
rotulos: ["Configuração", "Impostos", "IBS", "CBS", "Artigo criado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Fiscal/Contábil - KCS", "ERP"]
---

# Como configurar CBS e IBS com base de cálculo reduzida no ERP Sankhya

### Entendendo a base de cálculo reduzida para CBS e IBS

A **"CBS"** (Contribuição sobre Bens e Serviços) e o **"IBS"** (Imposto sobre Bens e Serviços) são os novos tributos da reforma tributária brasileira. Em determinadas situações, é possível aplicar **"redução na base de cálculo"** desses impostos, resultando em uma carga tributária menor para operações específicas.

### O que é base de cálculo reduzida?

A base de cálculo reduzida ocorre quando, por determinação legal ou benefício fiscal, aplica-se um percentual de redução sobre o valor que seria normalmente tributado. Por exemplo, se um produto tem valor de R$ 1.000,00 e há uma redução de 40% na base, o **"IBS"**/**"CBS"** será calculado sobre R$ 600,00.

### Composição da base de cálculo

Conforme as regras da reforma tributária, a base de cálculo do **"IBS"** e **"CBS"** é composta por:

| Operação | Campo |
| --- | --- |
| (+) | `vProd` — Valor dos produtos |
| (+) | `vServ` — Valor dos serviços |
| (+) | `vFrete` — Frete |
| (+) | `vSeg` — Seguro |
| (+) | `vOutro` — Outras despesas |
| (+) | `vII` — Imposto de Importação |
| (−) | `vDesc` — Desconto |
| (−) | `vPis` — PIS\* |
| (−) | `vCofins` — COFINS\* |
| (−) | `vICMS` — ICMS\* |
| (−) | `vICMSUFDest` — ICMS da UF de destino\* |
| (−) | `vFCP` — FCP\* |
| (−) | `vFCPUFDest` — FCP da UF de destino\* |
| (−) | `vICMSMono` — ICMS monofásico\* |
| (−) | `vISSQN` — ISSQN\* |
| (+) | `vIS` — Imposto Seletivo\* |

Os valores marcados com asterisco (\*) são deduzidos conforme indicadores específicos de cada operação.

### Configurando alíquotas com redução de base

Para aplicar base de cálculo reduzida no sistema Sankhya, siga as orientações abaixo:

### Cadastro de alíquotas de IBS e CBS

**(1)** Acesse a tela de **"Cadastro de Alíquotas IBS/CBS"** (Comercial Arquivo Tabelas Cadastro de Alíquotas IBS/CBS) e cadastre as alíquotas necessárias para sua operação.

**(2)** Configure alíquotas distintas para cada cenário:
- Alíquota com tributação integral (sem redução)
- Alíquota com percentual de redução aplicado (ex: redução de 40%, 60%, etc.)

**(3)** Informe o percentual de redução da base de cálculo no campo específico da alíquota, quando aplicável.

### Classificação tributária do produto

**(4)** Acesse o cadastro de **"Produtos"** (Configurações Cadastros Produtos) e localize o produto que terá tratamento diferenciado.

**(5)** Aba Impostos configure o **"Código Classificação Tributária Nacional"** do produto.

**(6)** Se necessário, utilize **"Grupo IBS/CBS"** para diferenciar produtos que, mesmo com o mesmo NCM, possuem tratamentos tributários distintos.

### Configuração do parceiro com benefício fiscal

**(7)** Acesse o cadastro de **"Parceiros"** (Configurações Cadastros Parceiros) e localize o cliente ou fornecedor que possui direito à redução.

**(8)** Identifique o parceiro com marcações específicas que indiquem benefícios fiscais, diferimento ou regime especial de tributação.

**(9)** Vincule o parceiro ao grupo tributário adequado, permitindo que o sistema identifique automaticamente o tratamento fiscal correto.

### Configuração do Tipo de Operação (TOP)

**(10)** Acesse a tela de **"Tipos de Operação"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) e configure os TOPs que utilizarão **"IBS"** e **"CBS"** com base reduzida.

- Habilite os campos **"IBS"** e **"CBS"** no **"Tipo de Operação"**.
- Configure os indicadores de composição de base conforme a legislação.
- Defina se haverá diferimento, devolução ou crédito presumido.

### Motor de seleção de alíquotas

O sistema Sankhya utiliza um motor de seleção de alíquotas que determina automaticamente qual alíquota aplicar com base em diversos critérios:

- **"NCM/NBS"** do produto
- Finalidade da operação
- Vigência da alíquota
- Características do parceiro
- Tipo de operação (TOP)

Quando uma operação é realizada, o sistema cruza todas essas informações e seleciona a alíquota correta, aplicando automaticamente a redução de base quando configurada.

### Cálculo e registro dos impostos

Após a seleção da alíquota correta, o sistema:

**(1)** Calcula a base de cálculo conforme a fórmula estabelecida.

**(2)** Aplica o percentual de redução (se configurado).

**(3)** Calcula o valor do **"IBS"** e **"CBS"** sobre a base reduzida.

**(4)** Registra os valores na tabela de impostos.

**(5)** Totaliza corretamente os valores no rodapé do documento fiscal.

**(6)** Gera memória de cálculo rastreável para auditoria.

### Validação e conferência

Após configurar o sistema, valide os cálculos verificando:

- Valores de **"IBS"** e **"CBS"** no item da nota;
- Base de cálculo com redução aplicada;
- Totalização no rodapé do documento;
- Registro fiscal com códigos de classificação tributária corretos;
- Resumo de impostos.

O sistema permite consultar os detalhes do cálculo através da opção **"Consultar/Alterar Dados do Imposto do Item da Nota"**, onde é possível verificar todos os componentes da base de cálculo e os percentuais aplicados.

### Considerações importantes

- A configuração correta de alíquotas, produtos, parceiros e **"TOP"** é fundamental para o cálculo adequado.
- O sistema suporta múltiplas alíquotas para o mesmo produto.
- A redução de base pode ser combinada com outros benefícios fiscais.
- Mantenha sempre a legislação atualizada no cadastro de alíquotas.
