---
id: "40497635266583"
titulo: "Uso do E-mail Corporativo no Sankhya Pass e no Workspace RH"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40497635266583-Uso-do-E-mail-Corporativo-no-Sankhya-Pass-e-no-Workspace-RH"
trilha: "Manual do Produto > Pessoas+ > Implantação e Acessos do Pessoas+ > Usuários e Permissões do Pessoas+"
atualizado_em: "2026-09-27T13:56:29Z"
rotulos: ["Segurança", "ID: br.com.sankhya.cadastro.funcionarios", "Configuração Funcionários", "Pessoal+", "Sankhya Pass", "Uso do E-mail Corporativo no Sankhya Pass e Workspace RH", "E-mail Corporativo", "Workspace RH"]
---

# Uso do E-mail Corporativo no Sankhya Pass e no Workspace RH

**Módulo:** Pessoal+
**Versão Mínima:**5.97.0 
**Caminho de Acesso:** Pessoal+ > Cadastros > Configuração Funcionários > Aba Pessoal
**ID da Tela:**br.com.sankhya.cadastro.funcionarios

---

### Descrição e Usabilidade

O campo **Email Corporativo** situado na tela **Configuração Funcionários**, aba **Pessoal**, seção **Contato** é utilizado como requisito para criação de acessos corporativos relacionados ao ecossistema Sankhya, especialmente nos processos de:

- criação do **Sankhya Pass**;
- liberação de acesso ao **Workspace RH**.

A funcionalidade garante que os acessos institucionais sejam vinculados exclusivamente ao endereço corporativo do colaborador, evitando o uso de e-mails pessoais em autenticações, integrações e processos internos.

O campo permanece opcional no cadastro do colaborador, porém torna-se **obrigatório** quando houver solicitação de **criação de acessos corporativos**.

![Imagem 1: O campo permanece opcional no cadastro do colaborador, porém torna-se obrigatório quando houver solicitação de criação…](https://ajuda.sankhya.com.br/hc/article_attachments/40498088429847)

A partir da versão **5.125**, o **Email Corporativo** também pode ser informado já na **Requisição de Admissão** (etapa Dados Principais) sendo levado para o cadastro do funcionário quando a admissão é efetivada, ficando disponível para a criação do Sankhya Pass e a liberação do Workspace RH.

### Regras de validação

Ao solicitar a criação do **Sankhya Pass** ou do acesso ao **Workspace RH**, o sistema verifica automaticamente se:

1. **existe um Email Corporativo preenchido no cadastro do colaborador;**

   | **⚠️** **Atenção**  Quando o cadastro possuir apenas o **Email** preenchido e não existir **Email Corporativo** informado:  - o acesso ao **Portal RH** poderá ser criado normalmente; - o **Sankhya Pass** e o **Workspace RH** não serão criados.  Nessa situação, o sistema exibirá uma mensagem informando que o campo não foi preenchido, por isso o Sankhya Pass e Workspace RH não foram criados. |
   | --- |
2. **o formato do e-mail é válido (identificação do usuário + caractere @ + domínio);**

   Exemplo: maria.silva@empresa.com.br
3. **o endereço não está vinculado a outro colaborador com CPF diferente;**

   Quando o e-mail corporativo já estiver vinculado a outro colaborador com CPF diferente:

   - o salvamento será bloqueado e uma mensagem será exibida informando que o e-mail corporativo já está associado a outro colaborador com CPF diferente.

   Quando os e-mails pertencem à mesma pessoa física:

   - o sistema permite utilizar o mesmo e-mail corporativo;
   - também permite e-mails diferentes entre registros do mesmo CPF.

Isso ocorre porque não existe validação de consistência entre múltiplos registros da mesma pessoa.

4. **o e-mail não está sendo utilizado por outro usuário Sankhya Pass.**

   Se o endereço informado já estiver sendo utilizado em outro usuário Sankhya Pass:

   - o sistema impedirá o salvamento e informará que já existe usuário Sankhya Pass com o e-mail corporativo utilizado.

Caso todas as validações sejam atendidas:

- o sistema cria o Sankhya Pass;
- o acesso ao Workspace RH é liberado normalmente.

### Pontos de Atenção

- O E-mail Corporativo não substitui o e-mail padrão já existente no cadastro.
- O campo é obrigatório apenas para processos relacionados ao Sankhya Pass e Workspace RH.
- O usuário para o Portal RH pode ser criado mesmo sem Email Corporativo.
- O campo aceita no máximo 80 caracteres.
- Alterações no Email Corporativo impactam diretamente processos futuros de criação e manutenção de acessos corporativos.

### Artigos Relacionados

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Portal RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433)
- [Workspace Sankhya RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/36777482253463)
