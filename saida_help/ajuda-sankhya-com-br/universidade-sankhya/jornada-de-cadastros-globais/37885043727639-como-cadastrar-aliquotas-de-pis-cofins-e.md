---
id: "37885043727639"
titulo: "Como cadastrar alíquotas de PIS, COFINS E CSLL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37885043727639-Como-cadastrar-al%C3%ADquotas-de-PIS-COFINS-E-CSLL"
trilha: "Universidade Sankhya > Jornada de Cadastros Globais"
atualizado_em: "2026-07-22T14:05:52Z"
rotulos: ["Alíquotas", "Configuração", "COFINS", "PIS", "CSLL", "Impostos", "Financeiro"]
---

# Como cadastrar alíquotas de PIS, COFINS E CSLL

## O que são as alíquotas de PIS, COFINS e CSLL?

São tributos federais cobrados das empresas para financiar benefícios sociais e a seguridade social. O PIS e a COFINS incidem sobre a receita bruta e variam conforme o regime tributário (cumulativo ou não cumulativo), enquanto a CSLL é calculada sobre o lucro líquido ajustado da empresa. Essas contribuições são obrigatórias e impactam diretamente na apuração dos tributos federais devidos.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/838432720)

#### Para realizar as movimentações corretamente, é necessário cadastrar as alíquotas de PIS e COFINS na base de dados. Siga o passo a passo abaixo para realizar esse registro.

**Atenção:** Nesta atividade prática, vamos criar três regras fiscais:

- **Duas regras de PIS e COFINS**: uma para o grupo **TODOS** e outra para o grupo **NÃO TRIBUTADO**;
- **Uma regra de CSLL**: destinada ao grupo **TODOS**.

Siga o passo a passo abaixo e realize as configurações conforme as orientações.

**1**. Cadastro da **Alíquota de PIS** de entradas - GRUPO: **TODOS**

- Acesse a tela **Alíquotas de PIS**

**Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS

- Clique em **+ Novo registro e preencha os campos:**
- **Grupo:** Defina um nome para identificação (**TODOS**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção Entrada
- **Tipo alíquota:** Selecione Percentual
- **Alíquota:** Informe a alíquota de PIS (ex: 1,65%)
- **Cód. sit. tributária:** Informe CST 50 (direito a crédito)
- Clique em **Salvar** para concluir.

**Obs.:** Ao salvar irá ser apresentado o popup do imposto similar(COFINS), valide o percentual e salve. Desta forma você irá cadastrar os dois impostos ao mesmo tempo.

**2.**Cadastro da **Alíquota de COFINS** de entradas - GRUPO: **TODOS**

- Acesse a tela **Alíquotas de COFINS**

**Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS

- Clique em **+ Novo registro e preencha os campos:**
- **Grupo:** Defina um nome para identificação (**TODOS**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção Entrada
- **Tipo alíquota:** Selecione Percentual
- **Alíquota:** Informe a alíquota de PIS (ex: 7,6%)
- **Cód. sit. tributária:** Informe CST 50 (direito a crédito)
- Clique em **Salvar** para concluir.

**3.** Cadastro da **Alíquota de PIS** de saídas - GRUPO: **TODOS**

- Clique em **+ Novo registro** e preencha os campos:
- **Grupo:** Defina um nome para identificação (**TODOS**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção **Saída**
- **Tipo alíquota:** Selecione **Percentual**
- **Alíquota:** Informe a alíquota de PIS (geralmente 1,65%)
- **Cód. sit. tributária:** Informe **CST 01** (alíquota normal)
- Clique em **Salvar** para concluir.

**Obs.:** Ao salvar irá ser apresentado o popup do imposto similar(COFINS), valide o percentual e salve. Desta forma você irá cadastrar os dois impostos ao mesmo tempo.

**4.** Cadastro da **Alíquota de COFINS** de saídas - GRUPO: **TODOS**

- Clique em **+ Novo registro** e preencha os campos:
- **Grupo:** Defina um nome para identificação (**TODOS**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção **Saída**
- **Tipo alíquota:** Selecione **Percentual**
- **Alíquota:** Informe a alíquota de PIS (geralmente 7,6%)
- **Cód. sit. tributária:** Informe **CST 01** (alíquota normal)
- Clique em **Salvar** para concluir.

**5.** Cadastro da **Alíquota de PIS** de entradas - GRUPO: **NÃO TRIBUTADO**

- Acesse a tela **Alíquotas de PIS**

**Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS

- Clique em **+ Novo registro e preencha os campos:**
- **Grupo:** Defina um nome para identificação (**NÃO TRIBUTADO**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção Entrada
- **Tipo alíquota:** Selecione Percentual
- **Alíquota:** Informe a alíquota de PIS - 0;
- **Cód. sit. tributária:** Informe Tributária - 98 - Outras entradas;
- Clique em **Salvar** para concluir

**Obs.:** Ao salvar irá ser apresentado o popup do imposto similar(COFINS), valide o percentual e salve. Desta forma você irá cadastrar os dois impostos ao mesmo tempo.

**6.** Cadastro da **Alíquota de COFINS** de entradas - GRUPO: **NÃO TRIBUTADO**

- Acesse a tela **Alíquotas de COFINS**

**Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS

- Clique em **+ Novo registro e preencha os campos:**
- **Grupo:** Defina um nome para identificação (**NÃO TRIBUTADO**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção Entrada
- **Tipo alíquota:** Selecione Percentual
- **Alíquota:** Informe a alíquota de COFINS - 0;
- **Cód. sit. tributária:** Informe Tributária - 98 - Outras entradas;
- Clique em **Salvar** para concluir

**7.** Cadastro da **Alíquota de PIS** de saídas - GRUPO: **NÃO TRIBUTADO**

- Clique em **+ Novo registro** e preencha os campos:
- **Grupo:** Defina um nome para identificação (**NÃO TRIBUTADO**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção **Saída**
- **Tipo alíquota:** Selecione **Percentual**
- **Alíquota:** Informe a alíquota de PIS - 0;
- **Cód. sit. tributária:** Informe **CST 01** (alíquota normal)
- Clique em **Salvar** para concluir

**8.** Cadastro da **Alíquota de COFINS** de saídas - GRUPO: **NÃO TRIBUTADO**

- Clique em **+ Novo registro** e preencha os campos:
- **Grupo:** Defina um nome para identificação (**NÃO TRIBUTADO**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção **Saída**
- **Tipo alíquota:** Selecione **Percentual**
- **Alíquota:** Informe a alíquota de COFINS - 0;
- **Cód. sit. tributária:** Informe **CST 01** (alíquota normal)
- Clique em **Salvar** para concluir

**9.** Cadastro da **Alíquota de CSLL -** de entradas - GRUPO: **TODOS**

**Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de CSLL

- Clique em **+ Novo registro** e preencha os campos:
- **Grupo:** Defina um nome para identificação (**TODOS**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção **Entrada**
- **Tipo alíquota:** Selecione **Percentual**
- **Alíquota:** Informe a alíquota de PIS - 0;
- Clique em **Salvar** para concluir.

**10.** Cadastro da **Alíquota de CSLL -** de saída - GRUPO: **TODOS**

**Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de CSLL

- Clique em **+ Novo registro** e preencha os campos:
- **Grupo:** Defina um nome para identificação (**TODOS**)
- **Empresa:** Informe a sua empresa.
- **Parceiro:** Informe 0
- **Tipo de Operação:** Informe 0
- **Tipo:** Selecione a opção **Saída.**
- **Tipo alíquota:** Selecione **Percentual**
- **Alíquota:** Informe a alíquota de PIS - 0;
- Clique em **Salvar** para concluir.

**11. Observações importantes**

- A prioridade para determinação de alíquota será: TOP, Parceiro e Empresa.
- É possível criar exceções específicas por CFOP ou por Parceiro.
- Para casos específicos, podem ser criados grupos diferentes com outras alíquotas.
- O sistema calculará **PIS/COFINS/CSLL** apenas após a confirmação da nota fiscal.
