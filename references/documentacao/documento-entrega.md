# Documento de Entrega e Checklist de Implantação

Documento emitido na conclusão do desenvolvimento para orientar o analista de implantação e registrar a homologação técnica.

---

## 1. Estrutura do Documento de Entrega

```markdown
# Documento de Entrega Técnica: [Nome da Solução/Add-on]

## 1. Identificação do Projeto
- **Cliente**: [Nome do Cliente]
- **Módulo / Add-on**: [Identificador do Addon]
- **Versão Entregue**: [ex: 1.0.0]
- **Data da Entrega**: [Data]
- **Desenvolvedor Responsável**: [Nome]

## 2. Resumo das Funcionalidades Entregues
- Descrição sucinta do que foi desenvolvido e colocado em produção/homologação.

## 3. Checklist Obrigatório de Implantação (Deploy)
- [ ] **1. Dicionário de Dados**:
      Executar scripts SQL ou importar metadados (tabelas e campos adicionais).
- [ ] **2. Instalação do Pacote**:
      Importar o arquivo `.addon` na tela *Gerenciador de Addons* ou disponibilizar o JAR em `Módulos Java`.
- [ ] **3. Parâmetros do Sistema**:
      Cadastrar/configurar parâmetros na tela *Preferências* (ex: `XYZ_URL_INTEGRACAO`, `XYZ_TOKEN`).
- [ ] **4. Permissões de Acesso**:
      Liberar acessos aos novos menus e botões de ação nas telas de *Controle de Acesso / Usuários*.
- [ ] **5. Reinício de Sessões / Servidor**:
      Reiniciar a aplicação ou recarregar os metadados do Sankhya caso necessário.

## 4. Roteiro de Homologação e Testes Realizados
- Cenário 1: [Descrição do teste e resultado obtido]
- Cenário 2: [Descrição do teste com anexo de evidência/print]

## 5. Termo de Homologação e Assinaturas
- Bloco para assinatura do desenvolvedor e do responsável pela validação no cliente.
```
