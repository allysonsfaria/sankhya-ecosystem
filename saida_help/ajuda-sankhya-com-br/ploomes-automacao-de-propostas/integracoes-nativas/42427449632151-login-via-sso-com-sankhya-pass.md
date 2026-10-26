---
id: "42427449632151"
titulo: "Login via SSO com Sankhya Pass"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427449632151-Login-via-SSO-com-Sankhya-Pass"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:36Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14136111", "sync_hash_29c65fd1268d"]
---

# Login via SSO com Sankhya Pass

## 1) Sobre a funcionalidade

O **Sankhya Pass** é uma solução de **Single Sign-On (SSO)** que permite acessar o Ploomes utilizando as mesmas credenciais do seu ecossistema Sankhya. O objetivo é centralizar o controle de identidade, aumentar a segurança e eliminar a fadiga de senhas, permitindo que o usuário entre na plataforma com apenas um clique, de forma rápida e segura.

---

## 2) Pré-requisitos

- Possuir uma conta ativa no **Sankhya Pass**.
- Possuir ao menos um usuário de perfil administrador cadastrado no **Sankhya Pass.**
- O e-mail do usuário no Sankhya deve ser **idêntico** ao e-mail cadastrado no Ploomes.
- Perfil de **Administrador** no Ploomes (apenas para a configuração inicial).

---

## 3) Configurando o Provedor de Login

Para habilitar o acesso via Sankhya Pass, um administrador deve seguir os passos abaixo:

### 3.1) Seleção do Provedor

1. Acesse **Configurações do Sistema**.
2. Clique em **Configuração de opções de login**.
3. Escolha o método de restrição:

   - **Permitir login por usuário Ploomes e SSO:** O usuário escolhe se quer entrar com a senha do Ploomes ou pelo Sankhya Pass.
   - **Permitir login apenas por SSO:** Obriga todos os usuários a utilizarem o Sankhya Pass (maior segurança)
4. No campo "Provedor de SSO", selecione a opção **Sankhya Pass**.

   [GIF animado: Imagem 1: No campo "Provedor de SSO", selecione a opção Sankhya Pass .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2183930231/f0c2e2d099773f3c2c574770c56b/chrome-capture-2026-03-20.gif?expires=1786536000&signature=f15bfa56de2aa61e9167c237a9d956fa8d562fd1fb1e43177491623450c6e4dc&req=diEvFcB9nYNcWPMW3nq%2BgTIZ4%2F1LNyNtLN0w8JnVD6e0US2j4bopLeApyPy%2F%0AckKKuX0bUaOm1i5%2B0CjLp3nkhLs%3D%0A)
5. Clique em **Salvar**.

**Atenção:** O Ploomes permite apenas um provedor de SSO ativo por vez. Se o **Microsoft Entra ID** estiver ativo, você precisará desativá-lo para conseguir selecionar o Sankhya Pass.

---

## 4) Utilizando a funcionalidade

### 4.1) Acessando o Ploomes via SSO

1. Na tela de login do Ploomes, localize o botão **"Entrar com Sankhya Pass"**.

   1. A partir do navegador

      ![Imagem 2: A partir do navegador](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2183942607/98ec79fb158da048f177d11c5436/image.png?expires=1786536000&signature=99a3fa8fa4caebaae358cd41c4baaed526555669648258ccbc032dcbd4a22b2f&req=diEvFcB6n4dfXvMW3nq%2BgWy8HusKDnOCNh1ULAetewRNkaB9U9nc1FNQFX%2BH%0ANv34MiIKvl0f%2BfM7e64KVOjdJHM%3D%0A)
   2. A partir do aplicativo

      ![Imagem 3: A partir do aplicativo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2226159789/cdcaa3ba8e43400fd2c01c1e36a9/image.png?expires=1786536000&signature=28f477c9e8a78160fe83e5c17ec11973700d02c2a2b25bb3b71e00223d2eccec&req=diIlEMh7lIZXUPMW3nq%2BgaZ0rWwaAUz0xt9%2B%2Fqr0C2fN3iOpJlfaLucXZg39%0A5bSZGu%2BBe%2BSVjbOtm3dPcGp181Y%3D%0A)
2. Você será redirecionado para a página oficial de autenticação do Sankhya.
3. Insira suas credenciais do Sankhya.
4. Após a validação, o sistema o levará automaticamente para a tela inicial do Ploomes.

### 4.2) Login Automático (Primeiro Acesso)

Se o seu e-mail já existe no Ploomes, não é necessário realizar nenhum vínculo manual. Ao clicar no botão e se autenticar no Sankhya, o Ploomes reconhece seu e-mail e inicia a sessão imediatamente. Caso o e-mail não exista no Ploomes, ele precisará ser criado para que a autenticação funcione.

---

## 5) Limitações

- **Conflito de SSO:** Não é possível manter as integrações Microsoft e Sankhya ativas simultaneamente no Ploomes.
- **Usuários Inativos:** Se um usuário estiver com o status "Inativo" no Ploomes, ele não conseguirá logar, mesmo que a autenticação no Sankhya seja bem-sucedida.
- **Criação de Contas:** O login via SSO não cria usuários automaticamente. O usuário deve ser previamente cadastrado no Ploomes com o e-mail correspondente.

---

## 6) F.A.Q.

### 6.1) Posso acessar o Ploomes com Sankhya Pass pelo navegador e pelo celular?

Sim! Ao ativar o login via Sankhya Pass, você poderá acessar o Ploomes tanto pela versão web (navegador) quanto pelo aplicativo mobile.

### 6.2) Por que a opção de provedor Sankhya Pass está desabilitada nas minhas configurações?

Isso ocorre quando o provedor Microsoft Entra ID (SSO Microsoft) está ativo. Para habilitar o Sankhya Pass, você deve desativar a integração Microsoft primeiro.

### 6.3) Tento logar e recebo a mensagem "E-mail ou senha incorretos", mas meus dados no Sankhya estão certos. O que houve?

Esta mensagem pode aparecer por dois motivos:

1) O e-mail utilizado no Sankhya não existe na base do Ploomes

2) O seu usuário no Ploomes está marcado como "Inativo". Verifique com seu administrador se o seu cadastro está correto.

### 6.4) Minha empresa usa Microsoft para logar no Sankhya. Como fica o Ploomes?

O Ploomes respeita o encadeamento. Você deve clicar em "Entrar com Sankhya Pass". O Sankhya solicitará seu login Microsoft e, após essa validação, o Sankhya enviará o sinal de "OK" para o Ploomes permitir seu acesso.

---

## 7) Dicas adicionais para melhores resultados

- **Padronização de E-mails:** Certifique-se de que todos os colaboradores utilizem o e-mail corporativo padrão em ambas as plataformas para evitar falhas no primeiro acesso.
- **Segurança Máxima:** Caso sua empresa já utilize o Sankhya como central de segurança, utilize a opção "Permitir login apenas por SSO" no Ploomes para garantir que ninguém acesse o CRM com senhas externas.

---

## 8) Glossário

- **SSO (Single Sign-On):** Mecanismo que permite ao usuário acessar vários sistemas com um único login e senha.
- **Sankhya Pass:** Provedor de identidade da Sankhya para autenticação unificada.
- **Token:** Um código de segurança invisível trocado entre o Sankhya e o Ploomes para provar que o usuário é quem diz ser.
