---
id: "37880483538711"
titulo: "Validação de parâmetros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880483538711-Valida%C3%A7%C3%A3o-de-par%C3%A2metros"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:32Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Preferências", "Prefeituras", "NFS-e"]
---

# Validação de parâmetros

## Preferências

As Preferências são o “painel de controle” da NFS-e. No faturamento, o Portal de Vendas lê essas definições para montar o RPS/XML e enviar à prefeitura no padrão certo. Com elas você indica, de forma centralizada, quem emite, onde tributa e como a nota será transmitida. Ajustes coerentes evitam rejeições e agilizam o retorno da autorização. 
**Importante:** Revise periodicamente quando houver mudança de regra municipal.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. **Acesse a tela Preferências**

**Menu:** Configuração  »  Avançado  »  Preferências

- Digite o parâmetro no campo (Chave ou Descrição e tecle ENTER) e pressione **ENTER** para carregar as informações.
- No lado direito da tela, será exibida a chave com as configurações correspondentes. Caso seja necessário alterá-las, faça as modificações e salve para confirmar.
- Clique no botão **"Salvar"** para concluir a alteração.

#### Preferências

- **DESTIMPNRETIDO -** “LIGADO”
  Nesta configuração os impostos federais serão destacados na nota, ainda que sejam retidos.
- **ENVEMAILNFSE -** “LIGADO”
  Ao ser habilitado, esse parâmetro configura o envio da nota por email ao parceiro após a sua confirmação.
- **NFSETMAXLOTE**
  Esta configuração determina o tempo de processamento da nota, ou seja, o tempo de retorno do webservice.
- **CIDISSCNAEEMP -** “LIGADO”
  Quando ligado, é obrigatório configurar a aba “CNAE Empresa”: defina o local de tributação do serviço e vincule, no cadastro do serviço, o CNAE correspondente.
- **NFSEMAXNOTALOTE**
  Nesta preferência define-se a quantidade máxima de notas permitidas em um unico lote.
- **NFSEISSRETZERO -** “DESLIGADO”
  Habilitado em situações muito específicas, permitirá o ISS retido 0 nas notas de serviço.
- **MUNALIQPERCNFSE**
  Este parâmetro define o formato da alíquota no XML da NFS-e: sem Código IBGE no campo “Texto”, a alíquota vai em fração decimal (5% → 0,05); com o Código IBGE, vai em percentual (5% → 5,00).
- **NFSEGERARBOLETO -** “Sim, para todos parceiros”
  A configuração deste parâmetro, configura a possibilidade e forma de  geração de boletos para NFS-e's.
- **CFGALIQSERVPROD -** “LIGADO”
  Define o escopo da alíquota na NFS-e: ligado, cada serviço/produto usa a sua do cadastro; desligado, prevalece a regra global da empresa.
- **NFSEAUTORENVIO -** “LIGADO”
  Se desativado, o sistema apenas protocola o lote de NFS-e e não aguarda o processamento da prefeitura; depois, o usuário deve usar “Buscar autorização” para trazer o retorno.
- **INCLUIALIPISCOF -** “LIGADO”
  Quando ativado, permite cadastrar as alíquotas de PIS e COFINS simultaneamente.
- **NFSEOBSITERPS - “**Descrição + obs. dos itens de serviços + obs. da nota"
  Este é um parâmetro que define o conteúdo a ser enviado na descrição dos itens da NFS-e (Nota Fiscal de Serviço Eletrônica).
- **NFSEOBSNOTRPS - “**Descrição + obs. dos itens de serviços + obs. da nota"
  Este parâmetro determina o conteúdo que será enviado na tag "servico":{"descricao"} da NFS-e (Nota Fiscal de Serviço Eletrônica).
