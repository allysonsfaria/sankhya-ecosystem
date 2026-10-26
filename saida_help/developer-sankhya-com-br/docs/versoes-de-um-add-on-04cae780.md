---
id: "https://developer.sankhya.com.br/docs/versoes-de-um-add-on"
titulo: "Gerenciar versões de um Add-on"
url: "https://developer.sankhya.com.br/docs/versoes-de-um-add-on"
atualizado_em: "2025-11-10T23:34:45.000Z"
---

# Gerenciar versões de um Add-on

Este documento descreve o funcionamento do versionamento de componentes do tipo **Add-on** no ecossistema Sankhya via **Portal do Desenvolvedor** e como essas versões são exibidas para os clientes na tela **Minhas Soluções** do **Sankhya Om**.

***

## 1. Estados de versão e visibilidade no Om

As versões de um componente Add-on podem estar nos seguintes estados:

* **Desenvolvimento**
* **Homologação**
* **Produção (Publicada)**
* **Inativa**

Clientes podem ser associados a uma versão específica de um Add-on para testes, conforme definido pelo parceiro desenvolvedor.

### Visibilidade no Om e flag de teste

A visibilidade no Om depende:

* do **estado da versão**
* da configuração da flag **“Instalação somente em ambiente de teste”**

**Funcionamento da flag 'Instalação somente em ambiente de teste':**

* **Homologação com flag ativa** → versão disponível apenas no ambiente de teste do cliente.
* **Homologação com flag inativa** → versão disponível em teste e produção para os clientes vinculados.

> Para ativar/inativar a flag, basta marcar/desmarcar o checkbox na edição da versão e salvar as alterações.
>
> ![](https://files.readme.io/6be0e68e10c6becacdbe8dbc046211d7779a688efd5c65a2ebce0ed7a3a6578e-image.png)
>
> <br />

***

### Estados e reflexos no Om

#### 🔹 Desenvolvimento

* Não aparece no Om (Minhas Soluções).
* Visível apenas no **Portal do Desenvolvedor**.
* Só aparece no Om quando publicado (teste ou produção).

#### 🔹 Homologação (Teste)

* Visível apenas para clientes **explicitamente associados** à versão.
* Com **flag 'Instalação somente em ambiente de teste' ativa** → disponível **somente em teste**.
* Com **flag 'Instalação somente em ambiente de teste' inativa** → disponível em **teste e produção**.

#### 🔹 Produção (Publicada)

* Visível para **todos os clientes** da solução (status *Período de teste* ou *Ativo*).
* Disponível no ambiente de **produção do Om**.

#### 🔹 Inativa

* Não aparece para **novas instalações**.
* Clientes já vinculados passam a ver a última versão publicada em Produção.
* Sempre deve existir **uma versão em Produção**.
* Para inativar uma versão publicada, é necessário promover outra versão para Produção.

***

## 2. Regras de associação

* **Cliente em nível de solução (sem associação específica):**\
  Sempre visualiza a **última versão publicada em Produção**.

* **Cliente associado a uma versão específica:**
  * Enquanto a versão estiver em **Homologação**, com flag ativa → visível apenas em **teste**.
  * Enquanto em **Homologação**, sem flag ativa → visível em **teste e produção**.
  * Se a versão for **inativada** → perde a associação e passa a ver a **última versão publicada**.

***

## 3. Experiência do cliente no Sankhya Om

Na tela **Minhas Soluções**, o cliente tem acesso a:

* Lista de soluções e versões disponíveis (respeitando as regras acima).
* Notificações quando há nova versão disponível para instalação.

***

## 📌 Resumo para parceiros

* **Minhas Soluções** é o ponto central onde clientes **visualizam, instalam e atualizam** Add-ons.
* **Homologação (Teste):** aparece apenas para clientes **explicitamente vinculados**.
  * Flag ativa → somente em teste.
  * Flag inativa → em teste e produção.
* **Produção (Publicada):** aparece para todos os clientes da solução com status *Período de teste* ou *Ativo*.
* Sempre deve existir **uma versão em Produção**.
* Para inativar uma versão publicada, é **obrigatório promover outra versão para Produção**.
