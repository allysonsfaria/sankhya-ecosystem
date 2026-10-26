# Desenvolvimento com Addon Studio 2.0 (Sankhya OM)

O Addon Studio é o ambiente e framework padrão para extensões e módulos Java no Sankhya OM.

## Anotações Principais e Ciclo de Vida

### 1. @ActionButton (Botão de Ação)
Executado quando o usuário clica em um botão configurado na tela (ex: Central de Vendas, Cadastro de Parceiros).

```java
package br.com.empresa.modulo.actions;

import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.extensions.actionbutton.Registro;
import br.com.sankhya.modelcore.auth.AuthenticationInfo;

public class ProcessarParceiroAction implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao contexto) throws Exception {
        Registro[] linhas = contexto.getLinhas();
        if (linhas == null || linhas.length == 0) {
            contexto.mostraErro("Selecione ao menos um registro para processar.");
            return;
        }

        for (Registro reg : linhas) {
            Object codParc = reg.getCampo("CODPARC");
            // Lógica de processamento
            reg.setCampo("AD_PROCESSADO", "S");
            reg.save();
        }

        contexto.setMensagemRetorno("Processamento concluído com sucesso!");
    }
}
```

### 2. @Listener (Eventos de Persistência / JAPE)
Intercepta o ciclo de vida dos registros no banco antes ou depois de inserir, atualizar ou excluir.

```java
package br.com.empresa.modulo.listeners;

import br.com.sankhya.extensions.eventogeral.EventoGeral;
import br.com.sankhya.extensions.eventogeral.PersistenceEvent;
import br.com.sankhya.jape.vo.DynamicVO;

public class ValidaParceiroListener implements EventoGeral {

    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        validarRegra(vo);
    }

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        DynamicVO oldVO = (DynamicVO) event.getOldVO(); // Valores anteriores
        validarRegra(vo);
    }

    @Override
    public void beforeDelete(PersistenceEvent event) throws Exception {}

    @Override
    public void afterInsert(PersistenceEvent event) throws Exception {}

    @Override
    public void afterUpdate(PersistenceEvent event) throws Exception {}

    @Override
    public void afterDelete(PersistenceEvent event) throws Exception {}

    private void validarRegra(DynamicVO vo) throws Exception {
        String cgcCpf = vo.asString("CGC_CPF");
        if (cgcCpf == null || cgcCpf.trim().isEmpty()) {
            throw new Exception("CPF/CNPJ é obrigatório para cadastro de parceiro.");
        }
    }
}
```

### 3. @BusinessRule (Regra de Negócio Comercial)
Validações avançadas no barramento de regras durante confirmação/faturamento de notas (TGFCAB).

```java
package br.com.empresa.modulo.rules;

import br.com.sankhya.modelcore.comercial.BarramentoRegras;
import br.com.sankhya.modelcore.comercial.Regra;

public class TravaLimiteCreditoRule implements Regra {

    @Override
    public void validar(BarramentoRegras barramento) throws Exception {
        // Objeto em validação
        Object nuNota = barramento.getNuNota();
        // Lógica de validação comercial
    }
}
```

### 4. @Callback (Confirmação / Faturamento de Documentos)
Reage a eventos do fluxo comercial (confirmar nota, cancelamento, faturamento).

### 5. @Job (Rotinas Agendadas)
Tarefas em segundo plano executadas pelo agendador do Sankhya.

```java
package br.com.empresa.modulo.jobs;

import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class SincronizacaoJob implements Job {
    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        try {
            // Execução agendada
        } catch (Exception e) {
            throw new JobExecutionException(e);
        }
    }
}
```

## Regras Críticas do Addon Studio
1. **Nunca prefixar com `AD_` em tabelas novas de Addon**: use prefixo de 3 a 5 letras próprio da sua empresa/solução (ex: `XYZ_TABELA`, `XYZ_CAMPO`). O prefixo `AD_` é reservado para campos do Dicionário criados diretamente pelo usuário final no Sankhya.
2. **Singletons Thread-Safe**: Classes de Serviço e Controladores são singletons. Nunca armazene estado do usuário em atributos de instância.
3. **Controle de Exceções**: Lance exceções com mensagens claras em português; o Sankhya captura e exibe em popup nativo na tela do usuário.
