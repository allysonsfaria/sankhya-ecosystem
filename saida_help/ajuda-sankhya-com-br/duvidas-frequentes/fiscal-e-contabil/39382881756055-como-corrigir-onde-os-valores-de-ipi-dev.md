---
id: "39382881756055"
titulo: "Como corrigir onde os valores de IPI devem ser registrados no Livro de ICMS ?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39382881756055-Como-corrigir-onde-os-valores-de-IPI-devem-ser-registrados-no-Livro-de-ICMS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-29T19:36:19Z"
rotulos: ["Configuração", "Fiscal", "IPI", "ICMS", "Impostos", "Preferências", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Como corrigir onde os valores de IPI devem ser registrados no Livro de ICMS ?

Ao gerar o **"Livro de ICMS/IPI"** (Livros Fiscais, Arquivos, Cadastro, Livro ICMS/IPI), os valores de IPI podem aparecer incorretamente **no campo que não seria o esperado**, localizado na aba **"ICMS/IPI/ST"**.

Este artigo orienta sobre como configurar corretamente o sistema para que os valores de IPI sejam registrados adequadamente nos livros fiscais, evitando falhas.

#### De onde vem a informação que será levada ao Livro Fiscal?

O campo **"Isentas de ICMS"** é alimentado durante a **geração dos Livros Fiscais** e depende de várias configurações que trabalham em conjunto:

##### Fontes de Informação:

1. **Preferências da Empresa** (aba "Livro de Entrada Cod. Tributação")
   - Define como cada código de tributação será escriturado.
   - Determina se os valores vão para "Isentas" ou "Outras".
2. **Tipo de Operação (TOP)** (aba "Livro Fiscal")
   - O campo **"Tipo de IPI"** determina o comportamento da escrituração.
   - Deve estar configurado como **"Com créd/déb de imposto"** para que as opções da empresa sejam consideradas.
3. **CST de IPI** da nota fiscal
   - O código de situação tributária define se o IPI tem direito a crédito ou não.
   - Influencia diretamente em qual coluna o valor será escriturado.
4. **Marcação "Usar Tratamento de Código de Tributação de IPI"**
   - Localizada na tela de Geração ICMS/IPI.
   - Quando ativa, o sistema considera as configurações específicas da empresa.

### Configurando o tratamento correto do IPI:

Para corrigir o registro dos valores de IPI, siga os passos abaixo:

#### 1. Preferências da empresa:

Esta é a configuração principal que determina onde os valores de IPI serão escriturados:

**Caminho:** Comercial » Preferências » Empresa.

1. Selecione a empresa que está com o problema.
2. Acesse a **aba "Livro de Entrada Cod.** "Tributação**"**

**Seção "Valor do IPI quando ICMS não incidir sobre IPI":**

Este campo define onde o valor do IPI será escriturado quando o ICMS não incide sobre o IPI:

**Opções disponíveis:**

- **Em branco**: mantém o comportamento nativo do sistema.
- **Observação**: O valor do IPI será registrado no campo "Observação" (não soma com a base reduzida do ICMS).
- **Isentas**: O valor do IPI será gerado no campo **"Isentas de ICMS"** ← **Esta é a causa do problema!**
- **Outras**: O valor do IPI será somado ao valor da base reduzida do ICMS e exibido no campo "Outras ICMS".
- **Nenhuma**: O IPI não é lançado nas colunas.

#### 2. Verificar a configuração da TOP (Tipo de Operação):

A TOP determina como o IPI será tratado na escrituração:

**Caminho:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP.

1. Localize a TOP utilizada nas notas que estão com problema.
2. Acesse a **aba "Livro Fiscal**".

**Campo "Tipo de IPI":**

Este campo é **fundamental** e sempre determinará como as opções da aba "Livro de Entrada Cod. "Tributação" irão se comportar:

**Opções disponíveis:**

- **"Com créd/déb de imposto"**: O sistema considerará as configurações da empresa (Preferências » Empresa » aba "Livro de Entrada Cod. Tributação")
- **"Sem créd/déb de imposto"**: O IPI não gerará crédito/débito.
- **Outras opções**: comportamentos específicos.
- **Aba "Impostos":**
- **Campo "Tem IPI":**
- ✅ Deve estar **marcado** se a operação envolve IPI.
- **Campo "Cálculo de ICMS, IPI, ISS, IBS, CBS e IS":**
- Configure conforme necessário:
  - **"Calcula e não digita"**: Sistema calcula automaticamente.
  - **"Calcula e Digita"**: Permite alteração manual.
  - **"Não** calcula **e digita"**: usuário informa manualmente.

#### 3. Verificar a Configuração do CST de IPI

O CST de IPI na nota fiscal influencia diretamente onde o valor será escriturado:

**Caminho:** Comercial » Preferências » Empresa.

1. Acesse a **aba "Livro de Entrada Cod.** "Tributação**"**
2. Localize a **sub-aba "IPI**".

**Nesta sub-aba, você verá os CSTs de IPI configurados:**

Cada CST pode ser classificado como:

- **Tributada**: IPI com direito a crédito.
- **Isentas**: IPI isento (valor vai para "Isentas" se configurado).
- **Outras**: IPI em outras situações (valor vai para "Outras" se configurado).
- **Nenhuma**: IPI não é escriturado.

#### 4. Verificar a Marcação na Geração ICMS/IPI

A marcação que ativa o tratamento especial de IPI:

**Caminho:** Fiscal » Livros Fiscais » Geração ICMS/IPI.

1. Acesse a tela de geração dos livros.
2. Localize a **aba "Geração ICMS/IPI**".

**Marcação "Usar Tratamento de Código Tributação de IPI Definido no Cadastro de Empresas?":**

- ✅ **Se estiver marcada**: O sistema usará as configurações da empresa (Preferências » Empresa » aba "Livro de Entrada Cod. Tributação")
- ⬜ **Se estiver desmarcada**: O sistema usará o comportamento padrão.

### Regenerando os lançamentos fiscais:

Após ajustar a configuração, é necessário regenerar os lançamentos para que as alterações sejam aplicadas aos registros existentes:

**(1)** Acesse a tela **"Geração ICMS/IPI"** (Livros Fiscais > Arquivos > Geração ICMS/IPI).
**(2)** Selecione o período desejado para regeneração.
**(3)** Execute a geração de lançamentos novamente para aplicar as novas configurações.

### Verificando os resultados:

Após regenerar os lançamentos, verifique se a correção foi aplicada corretamente:

**(1)** Acesse a tela **"Cadastro Livro ICMS/IPI"** (Livros Fiscais > Arquivos > Cadastro > Livro ICMS/IPI).
**(2)**  Verifique a aba **"ICMS/IPI/ST"**.
**(3)** Confirme se o campo do valor do IPI foi apresentado no campo esperado.
