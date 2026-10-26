---
id: "42948875881879"
titulo: "Crash - Erro ao acessar o Cabeçalho do Pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948875881879-Crash-Erro-ao-acessar-o-Cabe%C3%A7alho-do-Pedido"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:55:37Z"
rotulos: ["sync_hc", "vidya", "vidya_588916", "sync_hash_bc2963d21865"]
---

# Crash - Erro ao acessar o Cabeçalho do Pedido

## Mensagem apresentada

```
```
TypeError: undefined is not a function
```
```

## Imagem 1: (CsErrorBoundary) 2026-05-20T13:41:37.545Z Error: TypeError: undefined is not a function Source: at CsDatepicker… [CsErrorBoundary] 2026-05-20T13:41:37.545Z Error: TypeError: undefined is not a function Source: at CsDatepicker (address at index.android.bundle:1:5114664 Source frame: at CsDatepicker (address at index.android.bundle:1:5114664) Error stack: TypeError: undefined is not a function     at CsDatepicker (address at index.android.bundle:1:5114664)     at renderWithHooks (address at index.android.bundle:1:274691)     at updateFunctionComponent (address at index.android.bundle:1:284082)     at beginWork (address at index.android.bundle:1:291999)     at performUnitOfWork (address at index.android.bundle:1:310225)     at workLoopSync (address at index.android.bundle:1:309290)     at renderRootSync (address at index.android.bundle:1:309122)     at recoverFromConcurrentError (address at index.android.bundle:1:307408)     at flushSyncWorkAcrossRoots\_impl (address at index.android.bundle:1:263800)     at commitRootImpl (address at index.android.bundle:1:311856)     at commitRoot (address at index.android.bundle:1:311099)     at commitRootWhenReady (address at index.android.bundle:1:307601)     at performConcurrentWorkOnRoot (address at index.android.bundle:1:307028) Component stack: in CsDatepicker     in CsForm     in RCTView     in Unknown     in RCTScrollView     in ScrollView     in Wrapper     in KeyboardAwareScrollView     in RCTView     in Unknown     in OrderHeaderScreen     in CsErrorBoundary     in RCTView     in Unknown     in Suspense     in OrderCreateNavigator     in Suspense     in SuspenseLoading     in StaticContainer     in EnsureSingleNavigator     in SceneView     in RCTView     in Unknown     in RCTView     in Unknown     in RCTView     in Unknown     in CardSheet     in RCTView     in Unknown     in Unknown     in PanGestureHandler     in PanGestureHandler     in RCTView     in Unknown     in Unknown     in RCTView     in Unknown     in Card     in CardContainer     in RNSScreen     in Unknown     in Suspender     in Suspense     in Freeze     in DelayedFreeze     in InnerScreen     in Unknown     in MaybeScreen     in RNSScreenContainer     in ScreenContainer     in MaybeScreenContainer     in CardStack     in KeyboardManager     in SafeAreaProviderCompat     in RNGestureHandlerRootView     in GestureHandlerRootView     in StackView     in StackNavigator     in SalesNavigator     in StaticContainer     in EnsureSingleNavigator     in SceneView     in RCTView     in Unknown     in SceneContent     in RNSScreen     in Unknown     in Suspender     in Suspense     in Freeze     in DelayedFreeze     in InnerScreen     in Unknown     in ResourceSavingScene     in RNSScreenContainer     in ScreenContainer     in SafeAreaProviderCompat     in BottomTabView     in BottomTabNavigator     in TabNavigatorContent     in MainNavigatorContent     in TabBarVisibilityProvider     in MainNavigator     in StaticContainer     in EnsureSingleNavigator     in SceneView     in RCTView     in Unknown     in RCTView     in Unknown     in RCTView     in Unknown     in CardSheet     in RCTView     in Unknown     in Unknown     in PanGestureHandler     in PanGestureHandler     in RCTView     in Unknown     in Unknown     in RCTView     in Unknown     in Card     in CardContainer     in RNSScreen     in Unknown     in Suspender     in Suspense     in Freeze     in DelayedFreeze     in InnerScreen     in Unknown     in MaybeScreen     in RNSScreenContainer     in ScreenContainer     in MaybeScreenContainer     in CardStack     in KeyboardManager     in SafeAreaProviderCompat     in RNGestureHandlerRootView     in GestureHandlerRootView     in StackView     in StackNavigator     in HomeNavigator     in GpsCollectionProvider     in Routes     in CsErrorBoundary     in AlertVersion     in AlertProvider     in LoaderProvider     in EnsureSingleNavigator     in BaseNavigationContainer     in ThemeProvider     in NavigationContainer     in RCTView     in Unknown     in AndroidSafeBottom     in RNCSafeAreaProvider     in SafeAreaProvider     in RCTView     in Unknown     in ModalPanel     in ThemeProvider     in MappingProvider     in StyleProvider     in ApplicationProvider     in QueryClientProvider     in EngagementProvider     in ConnectionProvider     in Provider     in ThemeProvider     in RCTView     in Unknown     in Portal.Host     in Provider     in App     in RCTView     in Unknown     in AppContainer Quando ocorre

Esse problema normalmente acontece quando o cliente acessa ou sai da tela de **Cabeçalho do Pedido** no aplicativo.

---

## Causa do problema

Identificamos que, no layout utilizado no Sankhya, o campo:

```
```
DT.NEG (Data de Negociação)
```
```

está configurado com o valor padrão:

```
```
Data e Hora Atuais
```
```

Porém, para funcionamento correto do aplicativo, o campo deve estar configurado como:

```
```
Data Atual
```
```

Essa configuração incorreta faz com que o componente de data do aplicativo (`CsDatepicker`) apresente falha durante o carregamento do cabeçalho.

---

## Como corrigir

1. Acesse o **Configurador de Layout da Nota** no Sankhya.
2. Abra o layout utilizado pelo Vidya Force.
3. Localize o campo:

```
```
DT.NEG
```
```

4. Altere o valor padrão de:

```
```
Data e Hora Atuais
```
```

para:

```
```
Data Atual
```
```

5. Salve as alterações.
6. Realize uma nova sincronização no aplicativo.

---

## Resultado esperado

Após a alteração e sincronização, o acesso ao Cabeçalho do Pedido deverá ocorrer normalmente, sem apresentar o erro.
