---
id: "37784203186455"
titulo: "Controle por grade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37784203186455-Controle-por-grade"
trilha: "Universidade Sankhya > Jornada de Estoques"
atualizado_em: "2026-08-21T13:41:03Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Cadastro", "Grade"]
---

# Controle por grade

**Atenção!** Neste exemplo, será utilizado o produto **Cabo de Rede** com variações de cores e tamanho para demonstrar como realizar a configuração de grade no ERP Sankhya.
Lembre-se: você pode seguir as orientações abaixo e adaptá-las ao **produto e contexto da sua rotina**.

1. **Cadastro do Modelo de Grade**

| **Ação** | **Configuração** |
| --- | --- |
| Acesse a tela | **Menu:** Comercial » Arquivo » Cadastros » Modelo de Grade |
| Novo Registro | - Clique no botão **“+ Novo registro**” para incluir um novo registro. |
| **Campo** |  |
| Nome  Grade | - Informe uma descrição para a grade (Ex.: Cabos de rede). |
| Confirmação | - Clique no botão **Salvar.** |

2. **Cadastro de Dimensões**

| **Ação** | **Configuração** |
| --- | --- |
| Adicionar Dimensão: Tamanhos | - Na seção **“Dimensões”**, clique no botão “**+**” (**Cadastrar Dimensão Grade de Produtos**) para incluir um novo registro. |
| Dimensão | - Informe: **Tamanhos.** |
| Abreviação | - Informe: **TM.** |
| Tipo | - Selecione a opção **Coluna.** |
| Salvar | - Clique no botão **Salvar**. |
| Adicionar Dimensão: Cores | - Clique no botão “**+**” (**Cadastrar Dimensão Grade de Produtos**) para incluir um novo registro. |
| Dimensão | - Informe: **Cores.** |
| Abreviação | - Informe: **CR.** |
| Tipo | - Selecione a opção **Linha.** |
| Salvar | - Clique no botão **Salvar**. |
| **Observação** | É possível cadastrar até 2 dimensões por grade. |

3. **Dimensões - Tamanhos e Cores**

| **Ação** | **Configuração** |
| --- | --- |
| Selecionar Dimensão | - Na seção **Dimensões**, selecione **Tamanhos**. |
| Adicionar Variação | - Clique no botão “**+**” (**Cadastrar Variação Dimensão Grade de Produtos**)  para incluir um novo registro. |
| Variação | - Informe: **2M.** |
| Abreviação | - Informe: **2M.** |
| Permissões | - Marque os campos **Permite compra** e **Permite venda**. |
| Salvar | - Clique no botão **Salvar**. |
| Repetir o processo | - Repita o processo para os tamanhos: - **5m** (Abreviação: **5M**). - **10m** (Abreviação: **10M**). |

4. **Cadastro de Variações - Cores**

| **Ação** | **Configuração** |
| --- | --- |
| Selecionar Dimensão | - Na seção **Dimensões**, selecione **Cores**. |
| Adicionar Variação | - Clique no botão “**+**” (**Cadastrar Variação Dimensão Grade de Produtos**)  para incluir um novo registro. |
| Variação | - Informe: **Preto.** |
| Abreviação | - Informe: **PTO.** |
| Permissões | - Marque os campos **Permite compra** e **Permite venda**. |
| Confirmação | - Clique no botão **Salvar**. |
| Repetir o processo | - Repita o processo para a cor: **Amarelo** (Abreviação: **AM**). |

5. **Controle Adicional - Grade**

| **Etapa** | **Configuração** |
| --- | --- |
| Acesse a tela | **Menu:** Configurações » Cadastros » Produtos » Produtos |
| Selecionar Produto | - Selecione um produto disponível em sua base de dados para configurar o controle de estoque por grade.   Neste contexto, o produto referido é Cabo de rede. |
| Aba Medidas e Estoque | - Acesse a **sub-aba Controle Adicional**. |
| Controlar Por | - No campo **"Controlar Por"**, selecione **"Grade"**. |
| Modelo de grade | - Informe o modelo criado na etapa anterior. |
| Salvar | - Clique em **Salvar** para registrar as informações. |

6. **Controle por Grade e quantidade mínima**

| **Ação** | **Configuração** |
| --- | --- |
| Habilitar Grade Produto | - O sistema habilita o botão **Grade Produto**, permitindo a configuração de quantidades mínimas. |
| Configuração de Quantidades Mínimas | **Para cada cor:**   - **2m:** 100 unidades. - **5m:** 150 unidades. - **10m:** 50 unidades. |
| Configurações para Compra | - Na seção Configurações para compra, marque a opção **Usar grade padrão p/ quantidade mínima**. |
| Confirmação | - Clique em **Confirmar** para salvar todas as configurações. |
