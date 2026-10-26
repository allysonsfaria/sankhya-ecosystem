---
id: "39294679897623"
titulo: "Como o afastamento superior a 6 meses afeta o período aquisitivo de férias?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39294679897623-Como-o-afastamento-superior-a-6-meses-afeta-o-per%C3%ADodo-aquisitivo-de-f%C3%A9rias"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:38Z"
rotulos: ["Configuração", "Folha", "Afastamento", "Férias", "Artigo criado KCS", "Sankhya RH - KCS", "Legislação Trabalhista"]
---

# Como o afastamento superior a 6 meses afeta o período aquisitivo de férias?

Quando um colaborador permanece afastado por mais de **180 dias consecutivos** dentro de um período aquisitivo, ele **perde o direito às férias** daquele período, conforme previsto na legislação trabalhista brasileira. O sistema ERP Sankhya realiza automaticamente a quitação do período aquisitivo afetado e inicia um novo período aquisitivo com data posterior ao término do afastamento.

É importante compreender como o sistema processa essa situação e quais procedimentos devem ser adotados para garantir que os registros estejam corretos.

### Regra dos 180 dias de afastamento

Afastamentos **inferiores a 180 dias** não impedem o direito às férias. O colaborador mantém seu período aquisitivo normalmente e acumula dias de férias proporcionalmente ao tempo trabalhado. Apenas afastamentos que **ultrapassem 180 dias consecutivos** dentro do mesmo período aquisitivo resultam na perda do direito às férias.

Por exemplo, um funcionário que ficou afastado por 88 dias continua com direito às férias proporcionais. Já um colaborador afastado por 431 dias perde o direito a dois períodos aquisitivos completos.

### Processamento automático pelo sistema

O sistema ERP Sankhya realiza a **quitação automática do período aquisitivo** quando detecta um afastamento superior a 180 dias. Para que esse processo ocorra corretamente, é fundamental que o afastamento seja lançado com **apenas a data prevista informada**, sem a data fim.

Quando a data fim do afastamento é registrada posteriormente, o sistema recalcula automaticamente os períodos aquisitivos, quitando aqueles afetados e criando um novo período com início imediatamente após o término do afastamento.

### Ajuste manual quando necessário

Em situações onde a data fim do afastamento já estava informada e a quitação automática não ocorreu, é necessário realizar o ajuste manualmente. Siga os passos abaixo:

**(1)** Acesse a tela **"Painel de Configurações"** (Pessoal+ » Configurações » Painel de Configurações) e execute o **"Processo de quitação de férias"**. 

 O sistema possui um **Job interno** que processa a quitação automaticamente:

- Executa durante a noite
- Verifica colaboradores com afastamentos superiores a 180 dias
- Realiza a quitação do período aquisitivo

![Imagem 1: Realiza a quitação do período aquisitivo](https://ajuda.sankhya.com.br/hc/article_attachments/41585849280663)

**(2)** Após a quitação, acesse a tela **"Requisições"** (Pessoal+ » Rotinas Folha » Requisições) e abra um **"Novo período aquisitivo"** para o funcionário, com data de início posterior ao término do afastamento.

⚠️ Observações Importantes:

- **FPQUITAFERABERT** - "Quita férias na abertura para afastados" (Configurações » Avançado » Preferências)

Com este parâmetro **ligado**, o sistema realiza a quitação automática de férias e 13º salário para colaboradores afastados há mais de 180 dias.

###

No **Cadastro de Ocorrências**, a ocorrência utilizada para o afastamento deve ter a marcação:

- ☑️ **"Quita Férias por Afastamentos - Art. 133 CLT"**

### Lançamento do Afastamento

1. Acesse: **Pessoal+ » Rotinas » Registro de Ocorrências**
2. Selecione o colaborador afastado
3. Lance a ocorrência de afastamento (ex: Auxílio-doença, Acidente de trabalho)
4. **Importante**: NÃO preencha a data de término no momento do lançamento
5. A data fim só deve ser preenchida quando o colaborador retornar efetivamente

**Período Concessivo Garantido:**

- Se houver um período concessivo garantido antes do afastamento, este deverá ser aproveitado após o retorno do funcionário
- Haverá uma data limite para utilização dessas férias

**Retorno do Colaborador:**

- Ao inserir a data fim do afastamento no Registro de Ocorrências, caracteriza-se o retorno oficial
- Um novo período aquisitivo será iniciado automaticamente

**Prorrogação do Período Concessivo:**

- Para que haja prorrogação do período de gozo por afastamento, ative o parâmetro **FPOCOPRORROGADO** - "Dias afastados altera fim do período concessivo"

## 💡 Dica Adicional

### Casos de múltiplos períodos afetados

Quando o afastamento é muito prolongado, pode afetar **mais de um período aquisitivo**. Nestes casos, o sistema quita todos os períodos impactados e o próximo período aquisitivo inicia-se com data imediatamente posterior ao fim do afastamento.

É fundamental revisar cuidadosamente todos os períodos aquisitivos do colaborador para garantir que as datas estejam alinhadas com a legislação e com o histórico de afastamentos registrado no sistema.

### Verificação e correção de inconsistências

Caso identifique que o sistema calculou o período aquisitivo com **duração superior a 12 meses**, verifique se há registro de afastamento prolongado. Se houver inconsistências nos dados, acione o suporte para análise .
