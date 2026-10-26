---
id: "40105706129815"
titulo: "Configuração do Regime Especial de Tributação (NFS-e)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40105706129815-Configura%C3%A7%C3%A3o-do-Regime-Especial-de-Tributa%C3%A7%C3%A3o-NFS-e"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T16:28:48Z"
rotulos: ["Produtos", "ISS", "Configuração", "Parceiro", "Prefeituras", "NFS-e"]
---

# Configuração do Regime Especial de Tributação (NFS-e)

**Módulo:** Comercial › Cadastros

**Caminhos de acesso:**

› Configurações › Cadastros › Produtos › [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)

› Configurações › Cadastros › [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)

---

## O que é e para que serve

A configuração do Regime Especial de Tributação do ISS define a regra fiscal sob a qual a sua Nota Fiscal de Serviço (NFS-e) será autorizada pela prefeitura (ex: Ato Cooperado, Microempresa, Estimativa). Esta rotina flexível permite que você defina o regime de forma dinâmica: em vez de usar uma única regra engessada para toda a empresa, o sistema avalia a natureza do serviço prestado ou o perfil do seu cliente (tomador) para enviar a tag `<regEspTrib>` correta no momento do faturamento, evitando rejeições e paragens na emissão.

## Antes de começar

Para que a inteligência de hierarquia funcione e o sistema envie o regime configurado nos serviços e parceiros, existe um pré-requisito obrigatório no cadastro do município do tomador.

| **Atenção:**  Acesse ao **Cadastro de Cidades**, localize a cidade do seu cliente e certifique-se de que a marcação **"Enviar o Regime Especial de Tributação no json?"** está ativada. Se esta opção estiver desligada, o sistema ignorará as regras do Serviço e do Parceiro, assumindo o valor padrão definido nas Preferências da Empresa. |
| --- |

## Como o sistema escolhe o Regime (Hierarquia)

Durante o faturamento, o sistema não exige que todos os campos estejam preenchidos, pois trabalha com um esquema de "cascata" (fallback). Ele procura o código do Regime Especial respeitando estritamente a seguinte ordem:

1. [**Cadastro de Serviço**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)**:** (Prioridade Máxima). Se houver um regime definido aqui, ele anula as outras configurações.
2. [**Cadastro de Parceiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)**:** Se o serviço estiver com o regime "Vazio", o sistema procura a configuração no perfil do cliente.
3. [**Preferências da Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** Se tanto o Serviço quanto o Parceiro estiverem "Vazios" (ou se a flag da Cidade estiver desligada), o sistema enviará a configuração geral da empresa.

## Onde e como configurar

Para adequar a sua operação, você pode configurar o campo de Regime Especial nos dois níveis operacionais descritos abaixo.

### No [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) ([Aba Configurações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa))

#### Campo Regime esp. tributação ISS (NFS-e)

**O que faz:** Define a regra tributária de forma restrita à natureza do serviço faturado, sobrepondo-se ao perfil do cliente.

**Quando usar:** Utilize quando um serviço específico exigir um regime diferente do padrão (ex: um serviço classificado estritamente como "Ato Cooperado").

**Como funciona:** Selecione a opção correspondente à legislação do serviço:

- Vazio (Padrão: Passa a decisão para o Parceiro/Empresa)
- 0 - Nenhum
- 1 - Ato Cooperado (Cooperativa)
- 2 - Estimativa
- 3 - Microempresa Municipal
- 4 - Notário ou Registrador
- 5 - Profissional Autônomo
- 6 - Sociedade de Profissionais
- 9 - Outros

### No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) ([Aba Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal))

#### Campo Regime esp. tributação ISS (NFS-e)

**O que faz:** Atrasa o regime de tributação ao perfil do cliente (tomador do serviço), independentemente do serviço que ele esteja a comprar.

**Quando usar:** Utilize para clientes que exigem tratamento tributário diferenciado em todas as suas notas (desde que o serviço faturado esteja configurado como "Vazio").

| **Dica**  Novos registos nas telas de Serviço e Parceiro nascem sempre com este campo na opção **"Vazio"**. Isso garante a compatibilidade retroativa: se não alterar nada, o seu sistema continuará a faturar usando o comportamento padrão das Preferências da Empresa. |
| --- |
