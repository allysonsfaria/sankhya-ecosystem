---
id: "39372610835223"
titulo: "Cadastro de Alíquotas IBS/CBS - Registro Duplicado Após Atualização de Base"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39372610835223-Cadastro-de-Al%C3%ADquotas-IBS-CBS-Registro-Duplicado-Ap%C3%B3s-Atualiza%C3%A7%C3%A3o-de-Base"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-08-13T17:46:44Z"
rotulos: ["Configuração", "Atualização", "Impostos", "Erro", "Artigo criado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Fiscal/Contábil - KCS"]
---

# Cadastro de Alíquotas IBS/CBS - Registro Duplicado Após Atualização de Base

Este artigo aborda a situação em que, após uma atualização de base de dados, o sistema pode apresentar **registros duplicados** no cadastro de alíquotas de **IBS** (Imposto sobre Bens e Serviços) e **CBS** (Contribuição sobre Bens e Serviços), impedindo a criação ou edição de novas alíquotas.

**Causa**

Durante o processo de atualização de base ou migração de dados, podem ocorrer inconsistências que resultam em:

- Duplicação de registros de alíquotas com os mesmos parâmetros.
- Mensagens de erro ao tentar cadastrar novas alíquotas.
- Impedimento de edição de cadastros existentes.
- Conflitos de chave única no banco de dados.

### Identificação de Registros Duplicados

Para identificar se há registros duplicados:

**(1)** Acesse a tela **"Alíquotas de IBS"** (Livros Fiscais>Cadastros>Alíquotas de IBS) ou **"Alíquotas de CBS"** (Livros Fiscais>Cadastros>Alíquotas de CBS).

**(2)** Verifique se existem múltiplos registros com a mesma combinação de parâmetros: NCM ou NBS, Regime Tributário, CNAE, UF Destino, Município de Destino, Finalidade da Operação e Tipo de Operação.

**(3)** Ao tentar cadastrar uma nova alíquota, observe se o sistema exibe a mensagem: **"Já existe uma alíquota cadastrada com o ID xxx que possui as mesmas informações fornecidas**.**"**.

**Solução**

**(1)** Identifique os IDs dos registros duplicados nas telas de cadastro de alíquotas.

**(2)** Compare os registros duplicados e identifique qual deve ser mantido, preferencialmente o mais recente ou o que possui dados mais completos.

**(3)** Exclua os registros duplicados, mantendo apenas um registro válido para cada combinação de parâmetros.

**(4)** Após a exclusão, tente cadastrar ou editar novamente a alíquota desejada.

### Campos Obrigatórios no Cadastro

Na guia **"Tributação"**, quando a combinação de **"CST"** e **"Classificação Tributária"** tiver o indicador de tributação regular ativo, o grupo **"Tributação Regular"** deve ser preenchido com:

- **"CST"**
- **"Classificação Tributária"**
- **"Alíquota UF"**
- **"Alíquota Município"**

Para **"Alíquotas de CBS"**, o grupo deve conter: **"CST"**, **"Classificação Tributária"** e **"Alíquota"**.

A duplicidade de registros pode afetar o cálculo automático dos tributos. Certifique-se de que apenas um registro válido exista para cada combinação de parâmetros, garantindo a correta aplicação das alíquotas nos documentos fiscais.
