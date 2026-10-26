---
id: "13463034147607"
titulo: "Fluxo do Processo de Manutenção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13463034147607-Fluxo-do-Processo-de-Manuten%C3%A7%C3%A3o"
trilha: "Melhores Práticas > Documentação de processos"
atualizado_em: "2026-07-22T16:11:17Z"
rotulos: ["Processos", "Ordem de Serviço", "Processo de Manutenção", "Tech Lead QA Desenvolvedores; priorizar revisar comunicar", "Correção erros dúvidas Service Desk hotfixes curto prazo", "Ticket → N1 → N2 → OS Manutenção → Triagem → Diagnóstico → Solução → Teste", "Service Desk", "Sankhya", "Manutenção"]
---

# Fluxo do Processo de Manutenção

O processo de manutenção é um fluxo de atividades que envolvem a correção ou o esclarecimento de dúvidas dos produtos Sankhya. Através deste processo que entram as dúvidas provenientes do Service Desk (SD) ou das demandas de correções de funcionalidades nativas que não estão funcionando conforme o projeto e parametrização.

As características da Manutenção, são:

- Pequenos hotfix (correções de erros);
- Requerem entendimento do Problema (causa de 1 ou mais Incidentes);
- Têm ciclo de vida curto (semanas).

---

#### Informações e Priorização de Chamados

Caso você precise de:

- **Informações sobre o andamento de um chamado:** confira o status do seu ticket na Central de Ajuda;
- **Priorização de um chamado:** entre em contato com seu gerente de relacionamento.

---

#### Fluxo do Processo de Manutenção

O processo de Manutenção possui o seguinte fluxo de tarefas:

![Imagem 1: O processo de Manutenção possui o seguinte fluxo de tarefas:](https://ajuda.sankhya.com.br/hc/article_attachments/13765250375447)

---

Conforme fluxo acima, primeiramente, o Solicitante (Cliente/Consultor) abre no Zendesk um Ticket de Incidente ou Dúvida.

Esse Ticket é avaliado no **Nível 1 (N1)** do SD. Sendo que, caso o SD consiga tratá-lo, ele deve devolver para o Solicitante o esclarecimento da dúvida, a resolução do Incidente ou o paliativo do Problema. 

Porém, se for identificado no N1 que se trata de um Problema, o chamado é encaminhado para o **Nível 2 (N2)**. Neste nível, caso conheça a tratativa, deve-se devolver o chamado com ela. 

No entanto, se no N2 constatar que se trata de um Problema, deve-se abrir um Flow que gera automaticamente a OS de Manutenção. 

Após a abertura da OS para a Manutenção, são realizadas as seguinte etapas:

---

![Imagem 2: Após a abertura da OS para a Manutenção, são realizadas as seguinte etapas:](https://ajuda.sankhya.com.br/hc/article_attachments/13464832756631)

Na etapa de **"Triagem da OS"** é determinada a Célula responsável pela tratativa e verifica-se às pré-condições de Manutenção.

```
 Responsável: Tech Lead de QA de Sustentação
```

```
 Ações:
```

1. ```
   Determinar a Célula responsável pela tratativa;
   ```
2. ```
   Checar se o Teste de Entrada feito pelo SD está completo ou não;
   ```
3. ```
   Se estiver completo, enviar a OS para o Diagnóstico;
   ```
4. ```
   Se não estiver, se possível, fazer o Teste de Entrada;
   ```
5. ```
   Se não for possível fazer o Teste de Entrada, a OS será encaminhada para a
   Sessão de Diagnóstico para que seja repassado o feedback ao pessoal do SD.
   ```

---

![Imagem 3: Se não for possível fazer o Teste de Entrada, a OS será encaminhada para a Sessão de Diagnóstico para que seja…](https://ajuda.sankhya.com.br/hc/article_attachments/13465067857303)

O intuito dessa etapa é acelerar a curva de aprendizado dos envolvidos e acelerar o processo de tratativa da Indústria e do Service Desk. Além disso, é verificado se a OS se trata de uma dúvida ou um problema.

```
Responsável: QA de Sustentação (Responsável, mediador); DEV (perspectiva
técnica): Tech Lead ou Desenvolvedor Sênior da questão; PO/APO (perspectiva de
negócio) e SD (perspectiva de atendimento).
```

```
 Ações:
```

1. ```
   Se estiver faltando algo para o Diagnóstico, dar o feedback para o SD de forma
   clara, direta e transparente;
   ```
2. ```
   Se for uma dúvida, esclarecer e passar para a próxima;
   ```
3. ```
   Discussão do problema;
   ```
4. ```
   Se necessário, avaliar regras de negócio x código-fonte implementado;
   ```
5. ```
   Se for um problema, seguir para etapa de "Estruturar a Solução";
   ```
6. ```
   Se não, explicar por que não é um problema, orientar as devidas tratativas e
   retornar OS para SD.
   ```

---

![Imagem 4: Se não, explicar por que não é um problema, orientar as devidas tratativas e retornar OS para SD.](https://ajuda.sankhya.com.br/hc/article_attachments/13466125572119)

Nesta etapa, deve-se orientar os Desenvolvedores a realizar a Manutenção de forma mais eficaz e eficiente possível, e ainda, reduzir a curva de aprendizado dos Desenvolvedores novatos.

```
Responsável: TL ou DEV Sênior no assunto em questão
```

```
Ações:
```

1. ```
   Descrever em alto nível o ponto de Manutenção;
   ```
2. ```
   Descrever em alto nível a Manutenção a ser feita;
   ```
3. ```
   Orientar o DEV como ele pode ter certeza que a Manutenção foi bem sucedida.
   ```

---

![Imagem 5: Orientar o DEV como ele pode ter certeza que a Manutenção foi bem sucedida.](https://ajuda.sankhya.com.br/hc/article_attachments/13481348817943)

Esta etapa tem o intuito de reduzir o risco de retorno ou problemas decorrentes. Sendo que, é necessário que as Manutenções mais complexas e arriscadas sejam tratadas pelos veteranos (Pleno ou Sênior).

```
Responsável: Desenvolvedor Pleno, Sênior ou de Referência
```

```
Ações:
```

1. ```
   Realizar as OS priorizadas ou as mais antigas primeiro.
   ```

---

![Imagem 6: Realizar as OS priorizadas ou as mais antigas primeiro.](https://ajuda.sankhya.com.br/hc/article_attachments/13479863610263)

O propósito nesta etapa é permitir que os Desenvolvedores Júnior ou Pleno tratem as Manutenções mais simples e de menor risco, acelerar a curva de aprendizado e aumentar a produtividade.

```
Responsável: Desenvolvedor Júnior ou Pleno
```

```
Ações:
```

1. ```
   Realizar as OS priorizadas ou as mais antigas primeiro.
   ```

---

![Imagem 7: Realizar as OS priorizadas ou as mais antigas primeiro.](https://ajuda.sankhya.com.br/hc/article_attachments/13479950854551)

Nesta etapa, o objetivo é aumentar a efetividade das Manutenções.

```
Responsável: Desenvolvedor Sênior, de Referência ou Tech Lead
```

```
Ações:
```

1. ```
   Avaliar a Estruturação da Solução contra as modificações feitas no Código
   Fonte;
   ```
2. ```
   Avaliar pontos de risco e/ou futuros Incidentes, ou Problemas;
   ```
3. ```
   Dar feedback quando necessário.
   ```

---

![Imagem 8: Dar feedback quando necessário.](https://ajuda.sankhya.com.br/hc/article_attachments/13479996295319)

O propósito nesta etapa é preparar o pacote para realização do Teste de Saída.

```
Responsável: Desenvolvedor responsável pela Manutenção
```

```
Ações:
```

1. ```
   Checar se a correção não quebrou a versão da Branch da OS;
   ```
2. ```
   Preparar o pacote para realização do Teste de Saída.
   ```

---

![Imagem 9: Preparar o pacote para realização do Teste de Saída.](https://ajuda.sankhya.com.br/hc/article_attachments/13480252032279)

Esta etapa, tem como finalidade garantir que a Manutenção foi efetiva.

```
Responsável: Analista de QA
```

```
Ações:
```

1. ```
   Checar se o cenário do problema identificado na entrada da OS foi efetivamente
   tratado;
   ```
2. ```
   Checar se não teve efeito colateral.
   ```

---

![Imagem 10: Checar se não teve efeito colateral.](https://ajuda.sankhya.com.br/hc/article_attachments/13480354001303)

O intuito aqui, é garantir que a correção seja feita na versão original do problema e todas as versões superiores.

```
Responsável: Desenvolvedor responsável pela Manutenção
```

```
Ações:
```

1. ```
   Solicitar o MR para a versão da OS (P1: GA > RC e DEV, P2/P3: DEV) e todas as
   DEV das versões superiores.
   ```

---

![Imagem 11: Solicitar o MR para a versão da OS (P1: GA > RC e DEV, P2/P3: DEV) e todas as DEV das versões superiores.](https://ajuda.sankhya.com.br/hc/article_attachments/13480527667223)

O propósito nesta etapa é evitar que os Desenvolvedores iniciantes alterem incorretamente a GA.

```
Responsável: P1: TL ou SL responsável pela Célula da Manutenção; P2/P3: TL de QA
Delivery ou Merge Aprover da Semana.
```

```
Ações:
```

1. ```
   Checar as alterações feitas na Branch da OS;
   ```
2. ```
   Se estiver tudo certo, aprovar o MR.
   ```

---

![Imagem 12: Se estiver tudo certo, aprovar o MR.](https://ajuda.sankhya.com.br/hc/article_attachments/13962133369111)

Nesta etapa é realizada a comunicação do retorno para o cliente após a correção de um problema ser concluído.

```
Responsável: Service Desk (N1 e N2)
```

```
Ações:
```

1. ```
   O Service Desk envia para o cliente a correção feita com o Build para
   download. Essa comunicação ocorre no mesmo dia da correção para problemas P1
   (após a etapa “Teste de Saída”) e 1 dia útil após a correção para problemas
   P2 e P3 (após a etapa “Regressão Diária”).
   ```
