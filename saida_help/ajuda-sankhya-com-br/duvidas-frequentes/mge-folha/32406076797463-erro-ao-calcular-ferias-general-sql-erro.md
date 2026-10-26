---
id: "32406076797463"
titulo: "Erro ao Calcular Férias: General SQL errors. Nome de coluna 'E10106' inválido. Funcionário \"XXXX\" evento \"342\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32406076797463-Erro-ao-Calcular-F%C3%A9rias-General-SQL-errors-Nome-de-coluna-E10106-inv%C3%A1lido-Funcion%C3%A1rio-XXXX-evento-342"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:32:01Z"
rotulos: ["Configuração", "Eventos", "Fórmulas", "Folha", "eConsignado", "Erro ao Calcular Férias: General SQL errors. Nome de coluna 'E10106' inválido. Funcionário \"XXXX\" evento \"342\"", "General SQL errors", "Nome de coluna 'E10106' inválido", "Funcionário \"XXXX\" evento \"342\"", "Erro"]
---

# Erro ao Calcular Férias: General SQL errors. Nome de coluna 'E10106' inválido. Funcionário "XXXX" evento "342"

**MENSAGEM:**

General SQL errors. Nome de coluna 'E10106' inválido. Funcionário "XXXX" evento "342".

**SITUAÇÃO:**

Durante o cálculo das férias, ao processar o evento 342 - Prov. Créd. Trabalhador Férias, o sistema retorna o erro.

A  fórmula do evento 342 - **PROV DESC CRED TRAB. FÉRIAS** foi configurada desta forma:

IF(MemSetVar('ProvCred', ABS(FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &REFERE, 'M', **'E10106',**'V'))) > 0, IF(MemSetVar('MargemProv', **E1929** \* (35/100)) > 0, IF(MemGetVar('MargemProv') < MemGetVar('ProvCred'), MemGetVar('MargemProv'), MemGetVar('ProvCred')), 0), 0)  

**SOLUÇÃO:**

Corrija a fórmula substituindo corretamente os códigos:

**(1)** Utilize **apenas o número** para o evento lido no movimento: **10106**

- **FBM(...)** **está buscando o valor do evento** **lançado no movimento** → deve ser **apenas o número**, sem "E".

**(1)**Mantenha o **prefixo "E"** para o evento que representa uma **base**: **E1929**

- - **E1929** representa a **base de cálculo** composta por outros eventos → deve manter o "E".

#### Fórmula corrigida:

IF(MemSetVar('ProvCred', ABS(FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &REFERE, 'M', **'10106',**'V'))) > 0, IF(MemSetVar('MargemProv', **E1929** \* (35/100)) > 0, IF(MemGetVar('MargemProv') < MemGetVar('ProvCred'), MemGetVar('MargemProv'), MemGetVar('ProvCred')), 0), 0)  

**Após ajustar a fórmula, o cálculo das férias será executado corretamente, sem erro de coluna inválida.**

**CAUSA:**

Esse erro ocorre por conta da **utilização incorreta da referência ao código de evento** na fórmula associada ao evento 342.

Ao colocar **E10106**, o sistema tenta interpretar um evento no movimento exatamente com este, então percebe que **não existe**, resultando na mensagem: **Nome de coluna 'E10106' inválido.**
