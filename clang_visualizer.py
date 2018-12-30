import sys
import argparse

NUM_OF_CHECKS = 1000
checks_list = ['[abseil-string-find-startswith]',
               '[android-cloexec-accept]',
               '[android-cloexec-accept4]',
               '[android-cloexec-creat]',
               '[android-cloexec-dup]',
               '[android-cloexec-epoll-create]',
               '[android-cloexec-epoll-create1]',
               '[android-cloexec-fopen]',
               '[android-cloexec-inotify-init]',
               '[android-cloexec-inotify-init1]',
               '[android-cloexec-memfd-create]',
               '[android-cloexec-open]',
               '[android-cloexec-socket]',
               '[android-comparison-in-temp-failure-retry]',
               '[boost-use-to-string]',
               '[bugprone-argument-comment]',
               '[bugprone-assert-side-effect]',
               '[bugprone-bool-pointer-implicit-conversion]',
               '[bugprone-copy-constructor-init]',
               '[bugprone-dangling-handle]',
               '[bugprone-exception-escape]',
               '[bugprone-fold-init-type]',
               '[bugprone-forward-declaration-namespace]',
               '[bugprone-forwarding-reference-overload]',
               '[bugprone-inaccurate-erase]',
               '[bugprone-incorrect-roundings]',
               '[bugprone-integer-division]',
               '[bugprone-lambda-function-name]',
               '[bugprone-macro-parentheses]',
               '[bugprone-macro-repeated-side-effects]',
               '[bugprone-misplaced-operator-in-strlen-in-alloc]',
               '[bugprone-misplaced-widening-cast]',
               '[bugprone-move-forwarding-reference]',
               '[bugprone-multiple-statement-macro]',
               '[bugprone-parent-virtual-call]',
               '[bugprone-sizeof-container]',
               '[bugprone-sizeof-expression]',
               '[bugprone-string-constructor]',
               '[bugprone-string-integer-assignment]',
               '[bugprone-string-literal-with-embedded-nul]',
               '[bugprone-suspicious-enum-usage]',
               '[bugprone-suspicious-memset-usage]',
               '[bugprone-suspicious-missing-comma]',
               '[bugprone-suspicious-semicolon]',
               '[bugprone-suspicious-string-compare]',
               '[bugprone-swapped-arguments]',
               '[bugprone-terminating-continue]',
               '[bugprone-throw-keyword-missing]',
               '[bugprone-undefined-memory-manipulation]',
               '[bugprone-undelegated-constructor]',
               '[bugprone-unused-raii]',
               '[bugprone-unused-return-value]',
               '[bugprone-use-after-move]',
               '[bugprone-virtual-near-miss]',
               '[cert-dcl03-c]',
               '[cert-dcl21-cpp]',
               '[cert-dcl50-cpp]',
               '[cert-dcl54-cpp]',
               '[cert-dcl58-cpp]',
               '[cert-dcl59-cpp]',
               '[cert-env33-c]',
               '[cert-err09-cpp]',
               '[cert-err34-c]',
               '[cert-err52-cpp]',
               '[cert-err58-cpp]',
               '[cert-err60-cpp]',
               '[cert-err61-cpp]',
               '[cert-fio38-c]',
               '[cert-flp30-c]',
               '[cert-msc30-c]',
               '[cert-msc32-c]',
               '[cert-msc50-cpp]',
               '[cert-msc51-cpp]',
               '[cert-oop11-cpp]',
               '[cppcoreguidelines-avoid-goto]',
               '[cppcoreguidelines-c-copy-assignment-signature]',
               '[cppcoreguidelines-interfaces-global-init]',
               '[cppcoreguidelines-narrowing-conversions]',
               '[cppcoreguidelines-no-malloc]',
               '[cppcoreguidelines-owning-memory]',
               '[cppcoreguidelines-pro-bounds-array-to-pointer-decay]',
               '[cppcoreguidelines-pro-bounds-constant-array-index]',
               '[cppcoreguidelines-pro-bounds-pointer-arithmetic]',
               '[cppcoreguidelines-pro-type-const-cast]',
               '[cppcoreguidelines-pro-type-cstyle-cast]',
               '[cppcoreguidelines-pro-type-member-init]',
               '[cppcoreguidelines-pro-type-reinterpret-cast]',
               '[cppcoreguidelines-pro-type-static-cast-downcast]',
               '[cppcoreguidelines-pro-type-union-access]',
               '[cppcoreguidelines-pro-type-vararg]',
               '[cppcoreguidelines-slicing]',
               '[cppcoreguidelines-special-member-functions]',
               '[fuchsia-default-arguments]',
               '[fuchsia-header-anon-namespaces]',
               '[fuchsia-multiple-inheritance]',
               '[fuchsia-overloaded-operator]',
               '[fuchsia-restrict-system-includes]',
               '[fuchsia-statically-constructed-objects]',
               '[fuchsia-trailing-return]',
               '[fuchsia-virtual-inheritance]',
               '[google-build-explicit-make-pair]',
               '[google-build-namespaces]',
               '[google-build-using-namespace]',
               '[google-default-arguments]',
               '[google-explicit-constructor]',
               '[google-global-names-in-headers]',
               '[google-objc-avoid-throwing-exception]',
               '[google-objc-global-variable-declaration]',
               '[google-readability-braces-around-statements]',
               '[google-readability-casting]',
               '[google-readability-function-size]',
               '[google-readability-namespace-comments]',
               '[google-readability-todo]',
               '[google-runtime-int]',
               '[google-runtime-operator]',
               '[google-runtime-references]',
               '[hicpp-avoid-goto]',
               '[hicpp-braces-around-statements]',
               '[hicpp-deprecated-headers]',
               '[hicpp-exception-baseclass]',
               '[hicpp-explicit-conversions]',
               '[hicpp-function-size]',
               '[hicpp-invalid-access-moved]',
               '[hicpp-member-init]',
               '[hicpp-move-const-arg]',
               '[hicpp-multiway-paths-covered]',
               '[hicpp-named-parameter]',
               '[hicpp-new-delete-operators]',
               '[hicpp-no-array-decay]',
               '[hicpp-no-assembler]',
               '[hicpp-no-malloc]',
               '[hicpp-noexcept-move]',
               '[hicpp-signed-bitwise]',
               '[hicpp-special-member-functions]',
               '[hicpp-static-assert]',
               '[hicpp-undelegated-constructor]',
               '[hicpp-use-auto]',
               '[hicpp-use-emplace]',
               '[hicpp-use-equals-default]',
               '[hicpp-use-equals-delete]',
               '[hicpp-use-noexcept]',
               '[hicpp-use-nullptr]',
               '[hicpp-use-override]',
               '[hicpp-vararg]',
               '[llvm-header-guard]',
               '[llvm-include-order]',
               '[llvm-namespace-comment]',
               '[llvm-twine-local]',
               '[misc-definitions-in-headers]',
               '[misc-forwarding-reference-overload]',
               '[misc-incorrect-roundings]',
               '[misc-lambda-function-name]',
               '[misc-macro-parentheses]',
               '[misc-macro-repeated-side-effects]',
               '[misc-misplaced-const]',
               '[misc-new-delete-overloads]',
               '[misc-non-copyable-objects]',
               '[misc-redundant-expression]',
               '[misc-sizeof-container]',
               '[misc=sizeof-expression]',
               '[misc-static-assert]',
               '[misc-string-compare]',
               '[misc-string-integer-assignment]',
               '[misc-string-literal-with-embedded-nul]',
               '[misc-suspicious-missing-comma]',
               '[misc-suspicious-semicolon]',
               '[misc-suspicious-string-compare]',
               '[misc-swapped-arguments]',
               '[misc-throw-by-value-catch-by-reference]',
               '[misc-unconventional-assign-operator]',
               '[misc-undelegated-constructor]',
               '[misc-uniqueptr-reset-release]',
               '[misc-unused-alias-decls]',
               '[misc-unused-parameters]',
               '[misc-unused-using-decls]',
               '[modernize-avoid-bind]',
               '[modernize-deprecated-headers]',
               '[modernize-loop-convert]',
               '[modernize-make-shared]',
               '[modernize-make-unique]',
               '[modernize-pass-by-value]',
               '[modernize-raw-string-literal]',
               '[modernize-redundant-void-arg]',
               '[modernize-replace-auto-ptr]',
               '[modernize-replace-random-shuffle]',
               '[modernize-return-braced-init-list]',
               '[modernize-shrink-to-fit]',
               '[modernize-unary-static-assert]',
               '[modernize-use-auto]',
               '[modernize-use-bool-literals]',
               '[modernize-use-default-member-init]',
               '[modernize-use-emplace]',
               '[modernize-use-equals-default]',
               '[modernize-use-equals-delete]',
               '[modernize-use-noexcept]',
               '[modernize-use-nullptr]',
               '[modernize-use-override]',
               '[modernize-use-transparent-functors]',
               '[modernize-use-uncaught-exceptions]',
               '[modernize-use-using]',
               '[mpi-buffer-deref]',
               '[mpi-type-mismatch]',
               '[objc-avoid-nserror-init]',
               '[objc-avoid-spinlock]',
               '[objc-forbidden-subclassing]',
               '[objc-property-declaration]',
               '[performance-faster-string-find]',
               '[performance-for-range-copy]',
               '[performance-implicit-conversion-in-loop]',
               '[performance-inefficient-algorithm]',
               '[performance-inefficient-string-concatenation]',
               '[performance-inefficient-vector-operation]',
               '[performance-move-const-arg]',
               '[performance-move-constructor-init]',
               '[performance-noexcept-move-constructor]',
               '[performance-type-promotion-in-math-fn]',
               '[performance-unnecessary-copy-initialization]',
               '[performance-unnecessary-value-param]',
               '[portability-simd-intrinsics]',
               '[readability-avoid-const-params-in-decls]',
               '[readability-braces-around-statements]',
               '[readability-container-size-empty]',
               '[readability-delete-null-pointer]',
               '[readability-deleted-default]',
               '[readability-else-after-return]',
               '[readability-function-size]',
               '[readability-identifier-naming]',
               '[readability-implicit-bool-conversion]',
               '[readability-inconsistent-declaration-parameter-name]',
               '[readability-misleading-indentation]',
               '[readability-misplaced-array-index]',
               '[readability-named-parameter]',
               '[readability-non-const-parameter]',
               '[readability-redundant-control-flow]',
               '[readability-redundant-declaration]',
               '[readability-redundant-function-ptr-dereference]',
               '[readability-redundant-member-init]',
               '[readability-redundant-smartptr-get]',
               '[readability-redundant-string-cstr]',
               '[readability-redundant-string-init]',
               '[readability-simplify-boolean-expr]',
               '[readability-simplify-subscript-expr]',
               '[readability-static-accessed-through-instance]',
               '[readability-static-definition-in-anonymous-namespace]',
               '[readability-string-compare]',
               '[readability-uniqueptr-delete-release]',
               '[zircon-temporary-objects]', \
               # Core Analyzer checks (v8.0) as of 8/8/18. MAC OS X and Obj C core checks are not included below.
               '[clang-analyzer-core.CallAndMessage]', \
               '[clang-analyzer-core.DivideZero]', \
               '[clang-analyzer-core.NonNullParamChecker]', \
               '[clang-analyzer-core.NullDereference]', \
               '[clang-analyzer-core.StackAddressEscape]', \
               '[clang-analyzer-core.UndefinedBinaryOperatorResult]', \
               '[clang-analyzer-core.VLASize]', \
               '[clang-analyzer-core.uninitialized.ArraySubscript]', \
               '[clang-analyzer-core.uninitialized.Assign]', \
               '[clang-analyzer-core.uninitialized.Branch]', \
               '[clang-analyzer-core.uninitialized.CapturedBlockVariable]', \
               '[clang-analyzer-core.uninitialized.UndefReturn]', \
               '[clang-analyzer-cplusplus.NewDelete]', \
               '[clang-analyzer-cplusplus.NewDeleteLeaks]', \
               '[clang-analyzer-deadcode.DeadStores]', \
               '[clang-analyzer-nullability.NullPassedToNonnull]', \
               '[clang-analyzer-nullability.NullReturnedFromNonnull]', \
               '[clang-analyzer-nullability.NullableDereferenced]', \
               '[clang-analyzer-nullability.NullablePassedToNonnull]', \
               '[clang-analyzer-optin.mpi.MPI-Checker]', \
               '[clang-analyzer-security.FloatLoopCounter]', \
               '[clang-analyzer-security.insecureAPI.UncheckedReturn]', \
               '[clang-analyzer-security.insecureAPI.getpw]', \
               '[clang-analyzer-security.insecureAPI.gets]', \
               '[clang-analyzer-security.insecureAPI.mkstemp]', \
               '[clang-analyzer-security.insecureAPI.mktemp]', \
               '[clang-analyzer-security.insecureAPI.rand]', \
               '[clang-analyzer-security.insecureAPI.strcpy]', \
               '[clang-analyzer-security.insecureAPI.vfork]', \
               '[clang-analyzer-unix.API]', \
               '[clang-analyzer-unix.Malloc]', \
               '[clang-analyzer-unix.MallocSizeof]', \
               '[clang-analyzer-unix.MismatchedDeallocator]', \
               '[clang-analyzer-unix.Vfork]', \
               '[clang-analyzer-unix.cstring.BadSizeArg]', \
               '[clang-analyzer-unix.cstring.NullArg]', \
               # Clang Diagnostic checks (v8.0) as of 8/8/18.
               '[clang-diagnostic-error]', \
               '[clang-diagnostic-warning]', \
               '[clang-diagnostic-#pragma-messages]', \
               '[clang-diagnostic-#warnings]', \
               '[clang-diagnostic-CFString-literal]', \
               '[clang-diagnostic-CL4]', \
               '[clang-diagnostic-IndependentClass-attribute]', \
               '[clang-diagnostic-NSObject-attribute]', \
               '[clang-diagnostic-abi]', \
               '[clang-diagnostic-absolute-value]', \
               '[clang-diagnostic-abstract-final-class]', \
               '[clang-diagnostic-abstract-vbase-init]', \
               '[clang-diagnostic-address]', \
               '[clang-diagnostic-address-of-array-temporary]', \
               '[clang-diagnostic-address-of-packed-member]', \
               '[clang-diagnostic-address-of-temporary]', \
               '[clang-diagnostic-aggregate-return]', \
               '[clang-diagnostic-aligned-allocation-unavailable]', \
               '[clang-diagnostic-all]', \
               '[clang-diagnostic-alloca-with-align-alignof]', \
               '[clang-diagnostic-ambiguous-delete]', \
               '[clang-diagnostic-ambiguous-ellipsis]', \
               '[clang-diagnostic-ambiguous-macro]', \
               '[clang-diagnostic-ambiguous-member-template]', \
               '[clang-diagnostic-analyzer-incompatible-plugin]', \
               '[clang-diagnostic-anonymous-pack-parens]', \
               '[clang-diagnostic-arc]', \
               '[clang-diagnostic-arc-bridge-casts-disallowed-in-nonarc]', \
               '[clang-diagnostic-arc-maybe-repeated-use-of-weak]', \
               '[clang-diagnostic-arc-non-pod-memaccess]', \
               '[clang-diagnostic-arc-performSelector-leaks]', \
               '[clang-diagnostic-arc-repeated-use-of-weak]', \
               '[clang-diagnostic-arc-retain-cycles]', \
               '[clang-diagnostic-arc-unsafe-retained-assign]', \
               '[clang-diagnostic-array-bounds]', \
               '[clang-diagnostic-array-bounds-pointer-arithmetic]', \
               '[clang-diagnostic-asm]', \
               '[clang-diagnostic-asm-ignored-qualifier]', \
               '[clang-diagnostic-asm-operand-widths]', \
               '[clang-diagnostic-assign-enum]', \
               '[clang-diagnostic-assume]', \
               '[clang-diagnostic-at-protocol]', \
               '[clang-diagnostic-atomic-memory-ordering]', \
               '[clang-diagnostic-atomic-properties]', \
               '[clang-diagnostic-atomic-property-with-user-defined-accessor]', \
               '[clang-diagnostic-attribute-packed-for-bitfield]', \
               '[clang-diagnostic-attributes]', \
               '[clang-diagnostic-auto-disable-vptr-sanitizer]', \
               '[clang-diagnostic-auto-import]', \
               '[clang-diagnostic-auto-storage-class]', \
               '[clang-diagnostic-auto-var-id]', \
               '[clang-diagnostic-availability]', \
               '[clang-diagnostic-backend-plugin]', \
               '[clang-diagnostic-backslash-newline-escape]', \
               '[clang-diagnostic-bad-function-cast]', \
               '[clang-diagnostic-binary-literal]', \
               '[clang-diagnostic-bind-to-temporary-copy]', \
               '[clang-diagnostic-bitfield-constant-conversion]', \
               '[clang-diagnostic-bitfield-enum-conversion]', \
               '[clang-diagnostic-bitfield-width]', \
               '[clang-diagnostic-bitwise-op-parentheses]', \
               '[clang-diagnostic-block-capture-autoreleasing]', \
               '[clang-diagnostic-bool-conversion]', \
               '[clang-diagnostic-bool-conversions]', \
               '[clang-diagnostic-braced-scalar-init]', \
               '[clang-diagnostic-bridge-cast]', \
               '[clang-diagnostic-builtin-macro-redefined]', \
               '[clang-diagnostic-builtin-memcpy-chk-size]', \
               '[clang-diagnostic-builtin-requires-header]', \
               '[clang-diagnostic-c++-compat]', \
               '[clang-diagnostic-c++0x-compat]', \
               '[clang-diagnostic-c++0x-extensions]', \
               '[clang-diagnostic-c++0x-narrowing]', \
               '[clang-diagnostic-c++11-compat]', \
               '[clang-diagnostic-c++11-compat-deprecated-writable-strings]', \
               '[clang-diagnostic-c++11-compat-pedantic]', \
               '[clang-diagnostic-c++11-compat-reserved-user-defined-literal]', \
               '[clang-diagnostic-c++11-extensions]', \
               '[clang-diagnostic-c++11-extra-semi]', \
               '[clang-diagnostic-c++11-inline-namespace]', \
               '[clang-diagnostic-c++11-long-long]', \
               '[clang-diagnostic-c++11-narrowing]', \
               '[clang-diagnostic-c++14-binary-literal]', \
               '[clang-diagnostic-c++14-compat]', \
               '[clang-diagnostic-c++14-compat-pedantic]', \
               '[clang-diagnostic-c++14-extensions]', \
               '[clang-diagnostic-c++17-compat]', \
               '[clang-diagnostic-c++17-compat-mangling]', \
               '[clang-diagnostic-c++17-compat-pedantic]', \
               '[clang-diagnostic-c++17-extensions]', \
               '[clang-diagnostic-c++1y-extensions]', \
               '[clang-diagnostic-c++1z-compat]', \
               '[clang-diagnostic-c++1z-compat-mangling]', \
               '[clang-diagnostic-c++1z-extensions]', \
               '[clang-diagnostic-c++2a-compat]', \
               '[clang-diagnostic-c++2a-compat-pedantic]', \
               '[clang-diagnostic-c++2a-extensions]', \
               '[clang-diagnostic-c++98-c++11-c++14-c++17-compat]', \
               '[clang-diagnostic-c++98-c++11-c++14-c++17-compat-pedantic]', \
               '[clang-diagnostic-c++98-c++11-c++14-compat]', \
               '[clang-diagnostic-c++98-c++11-c++14-compat-pedantic]', \
               '[clang-diagnostic-c++98-c++11-compat]', \
               '[clang-diagnostic-c++98-c++11-compat-binary-literal]', \
               '[clang-diagnostic-c++98-c++11-compat-pedantic]', \
               '[clang-diagnostic-c++98-compat]', \
               '[clang-diagnostic-c++98-compat-bind-to-temporary-copy]', \
               '[clang-diagnostic-c++98-compat-local-type-template-args]', \
               '[clang-diagnostic-c++98-compat-pedantic]', \
               '[clang-diagnostic-c++98-compat-unnamed-type-template-args]', \
               '[clang-diagnostic-c11-extensions]', \
               '[clang-diagnostic-c99-compat]', \
               '[clang-diagnostic-c99-extensions]', \
               '[clang-diagnostic-cast-align]', \
               '[clang-diagnostic-cast-calling-convention]', \
               '[clang-diagnostic-cast-of-sel-type]', \
               '[clang-diagnostic-cast-qual]', \
               '[clang-diagnostic-char-align]', \
               '[clang-diagnostic-char-subscripts]', \
               '[clang-diagnostic-clang-cl-pch]', \
               '[clang-diagnostic-class-varargs]', \
               '[clang-diagnostic-comma]', \
               '[clang-diagnostic-comment]', \
               '[clang-diagnostic-comments]', \
               '[clang-diagnostic-compare-distinct-pointer-types]', \
               '[clang-diagnostic-complex-component-init]', \
               '[clang-diagnostic-conditional-type-mismatch]', \
               '[clang-diagnostic-conditional-uninitialized]', \
               '[clang-diagnostic-config-macros]', \
               '[clang-diagnostic-constant-conversion]', \
               '[clang-diagnostic-constant-logical-operand]', \
               '[clang-diagnostic-constexpr-not-const]', \
               '[clang-diagnostic-consumed]', \
               '[clang-diagnostic-conversion]', \
               '[clang-diagnostic-conversion-null]', \
               '[clang-diagnostic-coroutine]', \
               '[clang-diagnostic-coroutine-missing-unhandled-exception]', \
               '[clang-diagnostic-covered-switch-default]', \
               '[clang-diagnostic-cpp]', \
               '[clang-diagnostic-cstring-format-directive]', \
               '[clang-diagnostic-ctor-dtor-privacy]', \
               '[clang-diagnostic-cuda-compat]', \
               '[clang-diagnostic-custom-atomic-properties]', \
               '[clang-diagnostic-dangling-else]', \
               '[clang-diagnostic-dangling-field]', \
               '[clang-diagnostic-dangling-initializer-list]', \
               '[clang-diagnostic-date-time]', \
               '[clang-diagnostic-dealloc-in-category]', \
               '[clang-diagnostic-debug-compression-unavailable]', \
               '[clang-diagnostic-declaration-after-statement]', \
               '[clang-diagnostic-delegating-ctor-cycles]', \
               '[clang-diagnostic-delete-incomplete]', \
               '[clang-diagnostic-delete-non-virtual-dtor]', \
               '[clang-diagnostic-deprecated]', \
               '[clang-diagnostic-deprecated-attributes]', \
               '[clang-diagnostic-deprecated-declarations]', \
               '[clang-diagnostic-deprecated-dynamic-exception-spec]', \
               '[clang-diagnostic-deprecated-implementations]', \
               '[clang-diagnostic-deprecated-increment-bool]', \
               '[clang-diagnostic-deprecated-objc-isa-usage]', \
               '[clang-diagnostic-deprecated-objc-pointer-introspection]', \
               '[clang-diagnostic-deprecated-objc-pointer-introspection-performSelector]', \
               '[clang-diagnostic-deprecated-register]', \
               '[clang-diagnostic-deprecated-writable-strings]', \
               '[clang-diagnostic-direct-ivar-access]', \
               '[clang-diagnostic-disabled-macro-expansion]', \
               '[clang-diagnostic-disabled-optimization]', \
               '[clang-diagnostic-discard-qual]', \
               '[clang-diagnostic-distributed-object-modifiers]', \
               '[clang-diagnostic-div-by-zero]', \
               '[clang-diagnostic-division-by-zero]', \
               '[clang-diagnostic-dll-attribute-on-redeclaration]', \
               '[clang-diagnostic-dllexport-explicit-instantiation-decl]', \
               '[clang-diagnostic-dllimport-static-field-def]', \
               '[clang-diagnostic-documentation]', \
               '[clang-diagnostic-documentation-deprecated-sync]', \
               '[clang-diagnostic-documentation-html]', \
               '[clang-diagnostic-documentation-pedantic]', \
               '[clang-diagnostic-documentation-unknown-command]', \
               '[clang-diagnostic-dollar-in-identifier-extension]', \
               '[clang-diagnostic-double-promotion]', \
               '[clang-diagnostic-duplicate-decl-specifier]', \
               '[clang-diagnostic-duplicate-enum]', \
               '[clang-diagnostic-duplicate-method-arg]', \
               '[clang-diagnostic-duplicate-method-match]', \
               '[clang-diagnostic-duplicate-protocol]', \
               '[clang-diagnostic-dynamic-class-memaccess]', \
               '[clang-diagnostic-dynamic-exception-spec]', \
               '[clang-diagnostic-effc++]', \
               '[clang-diagnostic-embedded-directive]', \
               '[clang-diagnostic-empty-body]', \
               '[clang-diagnostic-empty-decomposition]', \
               '[clang-diagnostic-empty-translation-unit]', \
               '[clang-diagnostic-encode-type]', \
               '[clang-diagnostic-endif-labels]', \
               '[clang-diagnostic-enum-compare]', \
               '[clang-diagnostic-enum-compare-switch]', \
               '[clang-diagnostic-enum-conversion]', \
               '[clang-diagnostic-enum-too-large]', \
               '[clang-diagnostic-exceptions]', \
               '[clang-diagnostic-exit-time-destructors]', \
               '[clang-diagnostic-expansion-to-defined]', \
               '[clang-diagnostic-explicit-initialize-call]', \
               '[clang-diagnostic-explicit-ownership-type]', \
               '[clang-diagnostic-extended-offsetof]', \
               '[clang-diagnostic-extern-c-compat]', \
               '[clang-diagnostic-extern-initializer]', \
               '[clang-diagnostic-extra]', \
               '[clang-diagnostic-extra-qualification]', \
               '[clang-diagnostic-extra-semi]', \
               '[clang-diagnostic-extra-tokens]', \
               '[clang-diagnostic-fallback]', \
               '[clang-diagnostic-flag-enum]', \
               '[clang-diagnostic-flexible-array-extensions]', \
               '[clang-diagnostic-float-conversion]', \
               '[clang-diagnostic-float-equal]', \
               '[clang-diagnostic-float-overflow-conversion]', \
               '[clang-diagnostic-float-zero-conversion]', \
               '[clang-diagnostic-for-loop-analysis]', \
               '[clang-diagnostic-format]', \
               '[clang-diagnostic-format-extra-args]', \
               '[clang-diagnostic-format-invalid-specifier]', \
               '[clang-diagnostic-format-non-iso]', \
               '[clang-diagnostic-format-nonliteral]', \
               '[clang-diagnostic-format-pedantic]', \
               '[clang-diagnostic-format-security]', \
               '[clang-diagnostic-format-y2k]', \
               '[clang-diagnostic-format-zero-length]', \
               '[clang-diagnostic-format=2]', \
               '[clang-diagnostic-four-char-constants]', \
               '[clang-diagnostic-frame-larger-than=]', \
               '[clang-diagnostic-function-def-in-objc-container]', \
               '[clang-diagnostic-future-compat]', \
               '[clang-diagnostic-gcc-compat]', \
               '[clang-diagnostic-global-constructors]', \
               '[clang-diagnostic-gnu]', \
               '[clang-diagnostic-gnu-alignof-expression]', \
               '[clang-diagnostic-gnu-anonymous-struct]', \
               '[clang-diagnostic-gnu-array-member-paren-init]', \
               '[clang-diagnostic-gnu-auto-type]', \
               '[clang-diagnostic-gnu-binary-literal]', \
               '[clang-diagnostic-gnu-case-range]', \
               '[clang-diagnostic-gnu-complex-integer]', \
               '[clang-diagnostic-gnu-compound-literal-initializer]', \
               '[clang-diagnostic-gnu-conditional-omitted-operand]', \
               '[clang-diagnostic-gnu-designator]', \
               '[clang-diagnostic-gnu-empty-initializer]', \
               '[clang-diagnostic-gnu-empty-struct]', \
               '[clang-diagnostic-gnu-flexible-array-initializer]', \
               '[clang-diagnostic-gnu-flexible-array-union-member]', \
               '[clang-diagnostic-gnu-folding-constant]', \
               '[clang-diagnostic-gnu-imaginary-constant]', \
               '[clang-diagnostic-gnu-include-next]', \
               '[clang-diagnostic-gnu-label-as-value]', \
               '[clang-diagnostic-gnu-redeclared-enum]', \
               '[clang-diagnostic-gnu-statement-expression]', \
               '[clang-diagnostic-gnu-static-float-init]', \
               '[clang-diagnostic-gnu-string-literal-operator-template]', \
               '[clang-diagnostic-gnu-union-cast]', \
               '[clang-diagnostic-gnu-variable-sized-type-not-at-end]', \
               '[clang-diagnostic-gnu-zero-line-directive]', \
               '[clang-diagnostic-gnu-zero-variadic-macro-arguments]', \
               '[clang-diagnostic-header-guard]', \
               '[clang-diagnostic-header-hygiene]', \
               '[clang-diagnostic-idiomatic-parentheses]', \
               '[clang-diagnostic-ignored-attributes]', \
               '[clang-diagnostic-ignored-optimization-argument]', \
               '[clang-diagnostic-ignored-pragma-intrinsic]', \
               '[clang-diagnostic-ignored-pragmas]', \
               '[clang-diagnostic-ignored-qualifiers]', \
               '[clang-diagnostic-implicit]', \
               '[clang-diagnostic-implicit-atomic-properties]', \
               '[clang-diagnostic-implicit-conversion-floating-point-to-bool]', \
               '[clang-diagnostic-implicit-exception-spec-mismatch]', \
               '[clang-diagnostic-implicit-fallthrough]', \
               '[clang-diagnostic-implicit-fallthrough-per-function]', \
               '[clang-diagnostic-implicit-function-declaration]', \
               '[clang-diagnostic-implicit-int]', \
               '[clang-diagnostic-implicit-retain-self]', \
               '[clang-diagnostic-implicitly-unsigned-literal]', \
               '[clang-diagnostic-import]', \
               '[clang-diagnostic-import-preprocessor-directive-pedantic]', \
               '[clang-diagnostic-inaccessible-base]', \
               '[clang-diagnostic-include-next-absolute-path]', \
               '[clang-diagnostic-include-next-outside-header]', \
               '[clang-diagnostic-incompatible-exception-spec]', \
               '[clang-diagnostic-incompatible-function-pointer-types]', \
               '[clang-diagnostic-incompatible-library-redeclaration]', \
               '[clang-diagnostic-incompatible-ms-struct]', \
               '[clang-diagnostic-incompatible-pointer-types]', \
               '[clang-diagnostic-incompatible-pointer-types-discards-qualifiers]', \
               '[clang-diagnostic-incompatible-property-type]', \
               '[clang-diagnostic-incompatible-sysroot]', \
               '[clang-diagnostic-incomplete-implementation]', \
               '[clang-diagnostic-incomplete-module]', \
               '[clang-diagnostic-incomplete-umbrella]', \
               '[clang-diagnostic-inconsistent-dllimport]', \
               '[clang-diagnostic-inconsistent-missing-destructor-override]', \
               '[clang-diagnostic-inconsistent-missing-override]', \
               '[clang-diagnostic-increment-bool]', \
               '[clang-diagnostic-infinite-recursion]', \
               '[clang-diagnostic-init-self]', \
               '[clang-diagnostic-initializer-overrides]', \
               '[clang-diagnostic-injected-class-name]', \
               '[clang-diagnostic-inline]', \
               '[clang-diagnostic-inline-asm]', \
               '[clang-diagnostic-inline-new-delete]', \
               '[clang-diagnostic-instantiation-after-specialization]', \
               '[clang-diagnostic-int-conversion]', \
               '[clang-diagnostic-int-conversions]', \
               '[clang-diagnostic-int-to-pointer-cast]', \
               '[clang-diagnostic-int-to-void-pointer-cast]', \
               '[clang-diagnostic-integer-overflow]', \
               '[clang-diagnostic-invalid-command-line-argument]', \
               '[clang-diagnostic-invalid-constexpr]', \
               '[clang-diagnostic-invalid-iboutlet]', \
               '[clang-diagnostic-invalid-initializer-from-system-header]', \
               '[clang-diagnostic-invalid-ios-deployment-target]', \
               '[clang-diagnostic-invalid-noreturn]', \
               '[clang-diagnostic-invalid-offsetof]', \
               '[clang-diagnostic-invalid-or-nonexistent-directory]', \
               '[clang-diagnostic-invalid-partial-specialization]', \
               '[clang-diagnostic-invalid-pch]', \
               '[clang-diagnostic-invalid-pp-token]', \
               '[clang-diagnostic-invalid-source-encoding]', \
               '[clang-diagnostic-invalid-token-paste]', \
               '[clang-diagnostic-jump-seh-finally]', \
               '[clang-diagnostic-keyword-compat]', \
               '[clang-diagnostic-keyword-macro]', \
               '[clang-diagnostic-knr-promoted-parameter]', \
               '[clang-diagnostic-language-extension-token]', \
               '[clang-diagnostic-large-by-value-copy]', \
               '[clang-diagnostic-liblto]', \
               '[clang-diagnostic-literal-conversion]', \
               '[clang-diagnostic-literal-range]', \
               '[clang-diagnostic-local-type-template-args]', \
               '[clang-diagnostic-logical-not-parentheses]', \
               '[clang-diagnostic-logical-op-parentheses]', \
               '[clang-diagnostic-long-long]', \
               '[clang-diagnostic-loop-analysis]', \
               '[clang-diagnostic-macro-redefined]', \
               '[clang-diagnostic-main]', \
               '[clang-diagnostic-main-return-type]', \
               '[clang-diagnostic-malformed-warning-check]', \
               '[clang-diagnostic-many-braces-around-scalar-init]', \
               '[clang-diagnostic-max-unsigned-zero]', \
               '[clang-diagnostic-memsize-comparison]', \
               '[clang-diagnostic-method-signatures]', \
               '[clang-diagnostic-microsoft]', \
               '[clang-diagnostic-microsoft-anon-tag]', \
               '[clang-diagnostic-microsoft-cast]', \
               '[clang-diagnostic-microsoft-charize]', \
               '[clang-diagnostic-microsoft-comment-paste]', \
               '[clang-diagnostic-microsoft-const-init]', \
               '[clang-diagnostic-microsoft-cpp-macro]', \
               '[clang-diagnostic-microsoft-default-arg-redefinition]', \
               '[clang-diagnostic-microsoft-end-of-file]', \
               '[clang-diagnostic-microsoft-enum-forward-reference]', \
               '[clang-diagnostic-microsoft-enum-value]', \
               '[clang-diagnostic-microsoft-exception-spec]', \
               '[clang-diagnostic-microsoft-exists]', \
               '[clang-diagnostic-microsoft-explicit-constructor-call]', \
               '[clang-diagnostic-microsoft-extra-qualification]', \
               '[clang-diagnostic-microsoft-fixed-enum]', \
               '[clang-diagnostic-microsoft-flexible-array]', \
               '[clang-diagnostic-microsoft-goto]', \
               '[clang-diagnostic-microsoft-include]', \
               '[clang-diagnostic-microsoft-mutable-reference]', \
               '[clang-diagnostic-microsoft-pure-definition]', \
               '[clang-diagnostic-microsoft-redeclare-static]', \
               '[clang-diagnostic-microsoft-sealed]', \
               '[clang-diagnostic-microsoft-template]', \
               '[clang-diagnostic-microsoft-union-member-reference]', \
               '[clang-diagnostic-microsoft-unqualified-friend]', \
               '[clang-diagnostic-microsoft-using-decl]', \
               '[clang-diagnostic-microsoft-void-pseudo-dtor]', \
               '[clang-diagnostic-mismatched-new-delete]', \
               '[clang-diagnostic-mismatched-parameter-types]', \
               '[clang-diagnostic-mismatched-return-types]', \
               '[clang-diagnostic-mismatched-tags]', \
               '[clang-diagnostic-missing-braces]', \
               '[clang-diagnostic-missing-declarations]', \
               '[clang-diagnostic-missing-exception-spec]', \
               '[clang-diagnostic-missing-field-initializers]', \
               '[clang-diagnostic-missing-format-attribute]', \
               '[clang-diagnostic-missing-include-dirs]', \
               '[clang-diagnostic-missing-method-return-type]', \
               '[clang-diagnostic-missing-noescape]', \
               '[clang-diagnostic-missing-noreturn]', \
               '[clang-diagnostic-missing-prototype-for-cc]', \
               '[clang-diagnostic-missing-prototypes]', \
               '[clang-diagnostic-missing-selector-name]', \
               '[clang-diagnostic-missing-sysroot]', \
               '[clang-diagnostic-missing-variable-declarations]', \
               '[clang-diagnostic-module-build]', \
               '[clang-diagnostic-module-conflict]', \
               '[clang-diagnostic-module-file-config-mismatch]', \
               '[clang-diagnostic-module-file-extension]', \
               '[clang-diagnostic-module-import-in-extern-c]', \
               '[clang-diagnostic-modules-ambiguous-internal-linkage]', \
               '[clang-diagnostic-modules-import-nested-redundant]', \
               '[clang-diagnostic-most]', \
               '[clang-diagnostic-move]', \
               '[clang-diagnostic-msvc-include]', \
               '[clang-diagnostic-msvc-not-found]', \
               '[clang-diagnostic-multichar]', \
               '[clang-diagnostic-multiple-move-vbase]', \
               '[clang-diagnostic-narrowing]', \
               '[clang-diagnostic-nested-anon-types]', \
               '[clang-diagnostic-nested-externs]', \
               '[clang-diagnostic-new-returns-null]', \
               '[clang-diagnostic-newline-eof]', \
               '[clang-diagnostic-noexcept-type]', \
               '[clang-diagnostic-non-gcc]', \
               '[clang-diagnostic-non-literal-null-conversion]', \
               '[clang-diagnostic-non-modular-include-in-framework-module]', \
               '[clang-diagnostic-non-modular-include-in-module]', \
               '[clang-diagnostic-non-pod-varargs]', \
               '[clang-diagnostic-non-virtual-dtor]', \
               '[clang-diagnostic-nonnull]', \
               '[clang-diagnostic-nonportable-cfstrings]', \
               '[clang-diagnostic-nonportable-include-path]', \
               '[clang-diagnostic-nonportable-system-include-path]', \
               '[clang-diagnostic-nonportable-vector-initialization]', \
               '[clang-diagnostic-nsconsumed-mismatch]', \
               '[clang-diagnostic-nsreturns-mismatch]', \
               '[clang-diagnostic-null-arithmetic]', \
               '[clang-diagnostic-null-character]', \
               '[clang-diagnostic-null-conversion]', \
               '[clang-diagnostic-null-dereference]', \
               '[clang-diagnostic-null-pointer-arithmetic]', \
               '[clang-diagnostic-nullability]', \
               '[clang-diagnostic-nullability-completeness]', \
               '[clang-diagnostic-nullability-completeness-on-arrays]', \
               '[clang-diagnostic-nullability-declspec]', \
               '[clang-diagnostic-nullability-extension]', \
               '[clang-diagnostic-nullability-inferred-on-nested-type]', \
               '[clang-diagnostic-nullable-to-nonnull-conversion]', \
               '[clang-diagnostic-objc-autosynthesis-property-ivar-name-match]', \
               '[clang-diagnostic-objc-circular-container]', \
               '[clang-diagnostic-objc-cocoa-api]', \
               '[clang-diagnostic-objc-designated-initializers]', \
               '[clang-diagnostic-objc-flexible-array]', \
               '[clang-diagnostic-objc-forward-class-redefinition]', \
               '[clang-diagnostic-objc-interface-ivars]', \
               '[clang-diagnostic-objc-literal-compare]', \
               '[clang-diagnostic-objc-literal-conversion]', \
               '[clang-diagnostic-objc-macro-redefinition]', \
               '[clang-diagnostic-objc-messaging-id]', \
               '[clang-diagnostic-objc-method-access]', \
               '[clang-diagnostic-objc-missing-property-synthesis]', \
               '[clang-diagnostic-objc-missing-super-calls]', \
               '[clang-diagnostic-objc-multiple-method-names]', \
               '[clang-diagnostic-objc-noncopy-retain-block-property]', \
               '[clang-diagnostic-objc-nonunified-exceptions]', \
               '[clang-diagnostic-objc-property-implementation]', \
               '[clang-diagnostic-objc-property-implicit-mismatch]', \
               '[clang-diagnostic-objc-property-matches-cocoa-ownership-rule]', \
               '[clang-diagnostic-objc-property-no-attribute]', \
               '[clang-diagnostic-objc-property-synthesis]', \
               '[clang-diagnostic-objc-protocol-method-implementation]', \
               '[clang-diagnostic-objc-protocol-property-synthesis]', \
               '[clang-diagnostic-objc-protocol-qualifiers]', \
               '[clang-diagnostic-objc-readonly-with-setter-property]', \
               '[clang-diagnostic-objc-redundant-api-use]', \
               '[clang-diagnostic-objc-redundant-literal-use]', \
               '[clang-diagnostic-objc-root-class]', \
               '[clang-diagnostic-objc-string-compare]', \
               '[clang-diagnostic-objc-string-concatenation]', \
               '[clang-diagnostic-objc-unsafe-perform-selector]', \
               '[clang-diagnostic-odr]', \
               '[clang-diagnostic-old-style-cast]', \
               '[clang-diagnostic-old-style-definition]', \
               '[clang-diagnostic-opencl-unsupported-rgba]', \
               '[clang-diagnostic-openmp-clauses]', \
               '[clang-diagnostic-openmp-loop-form]', \
               '[clang-diagnostic-openmp-target]', \
               '[clang-diagnostic-option-ignored]', \
               '[clang-diagnostic-out-of-line-declaration]', \
               '[clang-diagnostic-out-of-scope-function]', \
               '[clang-diagnostic-over-aligned]', \
               '[clang-diagnostic-overflow]', \
               '[clang-diagnostic-overlength-strings]', \
               '[clang-diagnostic-overloaded-shift-op-parentheses]', \
               '[clang-diagnostic-overloaded-virtual]', \
               '[clang-diagnostic-override-module]', \
               '[clang-diagnostic-overriding-method-mismatch]', \
               '[clang-diagnostic-overriding-t-option]', \
               '[clang-diagnostic-packed]', \
               '[clang-diagnostic-padded]', \
               '[clang-diagnostic-parentheses]', \
               '[clang-diagnostic-parentheses-equality]', \
               '[clang-diagnostic-partial-availability]', \
               '[clang-diagnostic-pass]', \
               '[clang-diagnostic-pass-analysis]', \
               '[clang-diagnostic-pass-failed]', \
               '[clang-diagnostic-pass-missed]', \
               '[clang-diagnostic-pch-date-time]', \
               '[clang-diagnostic-pedantic]', \
               '[clang-diagnostic-pedantic-core-features]', \
               '[clang-diagnostic-pessimizing-move]', \
               '[clang-diagnostic-pointer-arith]', \
               '[clang-diagnostic-pointer-bool-conversion]', \
               '[clang-diagnostic-pointer-sign]', \
               '[clang-diagnostic-pointer-to-int-cast]', \
               '[clang-diagnostic-pointer-type-mismatch]', \
               '[clang-diagnostic-potentially-evaluated-expression]', \
               '[clang-diagnostic-pragma-clang-attribute]', \
               '[clang-diagnostic-pragma-once-outside-header]', \
               '[clang-diagnostic-pragma-pack]', \
               '[clang-diagnostic-pragma-pack-suspicious-include]', \
               '[clang-diagnostic-pragma-system-header-outside-header]', \
               '[clang-diagnostic-pragmas]', \
               '[clang-diagnostic-predefined-identifier-outside-function]', \
               '[clang-diagnostic-private-extern]', \
               '[clang-diagnostic-private-header]', \
               '[clang-diagnostic-private-module]', \
               '[clang-diagnostic-profile-instr-missing]', \
               '[clang-diagnostic-profile-instr-out-of-date]', \
               '[clang-diagnostic-profile-instr-unprofiled]', \
               '[clang-diagnostic-property-access-dot-syntax]', \
               '[clang-diagnostic-property-attribute-mismatch]', \
               '[clang-diagnostic-protocol]', \
               '[clang-diagnostic-protocol-property-synthesis-ambiguity]', \
               '[clang-diagnostic-qualified-void-return-type]', \
               '[clang-diagnostic-range-loop-analysis]', \
               '[clang-diagnostic-readonly-iboutlet-property]', \
               '[clang-diagnostic-receiver-expr]', \
               '[clang-diagnostic-receiver-forward-class]', \
               '[clang-diagnostic-redeclared-class-member]', \
               '[clang-diagnostic-redundant-decls]', \
               '[clang-diagnostic-redundant-move]', \
               '[clang-diagnostic-redundant-parens]', \
               '[clang-diagnostic-register]', \
               '[clang-diagnostic-reinterpret-base-class]', \
               '[clang-diagnostic-remark-backend-plugin]', \
               '[clang-diagnostic-reorder]', \
               '[clang-diagnostic-requires-super-attribute]', \
               '[clang-diagnostic-reserved-id-macro]', \
               '[clang-diagnostic-reserved-user-defined-literal]', \
               '[clang-diagnostic-retained-language-linkage]', \
               '[clang-diagnostic-return-stack-address]', \
               '[clang-diagnostic-return-type]', \
               '[clang-diagnostic-return-type-c-linkage]', \
               '[clang-diagnostic-rtti-for-exceptions]', \
               '[clang-diagnostic-sanitize-address]', \
               '[clang-diagnostic-section]', \
               '[clang-diagnostic-selector]', \
               '[clang-diagnostic-selector-type-mismatch]', \
               '[clang-diagnostic-self-assign]', \
               '[clang-diagnostic-self-assign-field]', \
               '[clang-diagnostic-self-move]', \
               '[clang-diagnostic-semicolon-before-method-body]', \
               '[clang-diagnostic-sentinel]', \
               '[clang-diagnostic-sequence-point]', \
               '[clang-diagnostic-serialized-diagnostics]', \
               '[clang-diagnostic-shadow]', \
               '[clang-diagnostic-shadow-all]', \
               '[clang-diagnostic-shadow-field]', \
               '[clang-diagnostic-shadow-field-in-constructor]', \
               '[clang-diagnostic-shadow-field-in-constructor-modified]', \
               '[clang-diagnostic-shadow-ivar]', \
               '[clang-diagnostic-shadow-uncaptured-local]', \
               '[clang-diagnostic-shift-count-negative]', \
               '[clang-diagnostic-shift-count-overflow]', \
               '[clang-diagnostic-shift-negative-value]', \
               '[clang-diagnostic-shift-op-parentheses]', \
               '[clang-diagnostic-shift-overflow]', \
               '[clang-diagnostic-shift-sign-overflow]', \
               '[clang-diagnostic-shorten-64-to-32]', \
               '[clang-diagnostic-sign-compare]', \
               '[clang-diagnostic-sign-conversion]', \
               '[clang-diagnostic-sign-promo]', \
               '[clang-diagnostic-signed-enum-bitfield]', \
               '[clang-diagnostic-sizeof-array-argument]', \
               '[clang-diagnostic-sizeof-array-decay]', \
               '[clang-diagnostic-sizeof-pointer-memaccess]', \
               '[clang-diagnostic-slash-u-filename]', \
               '[clang-diagnostic-sometimes-uninitialized]', \
               '[clang-diagnostic-source-uses-openmp]', \
               '[clang-diagnostic-spir-compat]', \
               '[clang-diagnostic-stack-protector]', \
               '[clang-diagnostic-static-float-init]', \
               '[clang-diagnostic-static-in-inline]', \
               '[clang-diagnostic-static-inline-explicit-instantiation]', \
               '[clang-diagnostic-static-local-in-inline]', \
               '[clang-diagnostic-static-self-init]', \
               '[clang-diagnostic-strict-aliasing]', \
               '[clang-diagnostic-strict-aliasing=0]', \
               '[clang-diagnostic-strict-aliasing=1]', \
               '[clang-diagnostic-strict-aliasing=2]', \
               '[clang-diagnostic-strict-overflow]', \
               '[clang-diagnostic-strict-overflow=0]', \
               '[clang-diagnostic-strict-overflow=1]', \
               '[clang-diagnostic-strict-overflow=2]', \
               '[clang-diagnostic-strict-overflow=3]', \
               '[clang-diagnostic-strict-overflow=4]', \
               '[clang-diagnostic-strict-overflow=5]', \
               '[clang-diagnostic-strict-prototypes]', \
               '[clang-diagnostic-strict-prototypes]', \
               '[clang-diagnostic-strict-selector-match]', \
               '[clang-diagnostic-string-compare]', \
               '[clang-diagnostic-string-conversion]', \
               '[clang-diagnostic-string-plus-char]', \
               '[clang-diagnostic-string-plus-int]', \
               '[clang-diagnostic-strlcpy-strlcat-size]', \
               '[clang-diagnostic-strncat-size]', \
               '[clang-diagnostic-super-class-method-mismatch]', \
               '[clang-diagnostic-switch]', \
               '[clang-diagnostic-switch-bool]', \
               '[clang-diagnostic-switch-default]', \
               '[clang-diagnostic-switch-enum]', \
               '[clang-diagnostic-sync-fetch-and-nand-semantics-changed]', \
               '[clang-diagnostic-synth]', \
               '[clang-diagnostic-tautological-compare]', \
               '[clang-diagnostic-tautological-constant-compare]', \
               '[clang-diagnostic-tautological-constant-out-of-range-compare]', \
               '[clang-diagnostic-tautological-overlap-compare]', \
               '[clang-diagnostic-tautological-pointer-compare]', \
               '[clang-diagnostic-tautological-undefined-compare]', \
               '[clang-diagnostic-tautological-unsigned-enum-zero-compare]', \
               '[clang-diagnostic-tautological-unsigned-zero-compare]', \
               '[clang-diagnostic-tentative-definition-incomplete-type]', \
               '[clang-diagnostic-thread-safety]', \
               '[clang-diagnostic-thread-safety-analysis]', \
               '[clang-diagnostic-thread-safety-attributes]', \
               '[clang-diagnostic-thread-safety-beta]', \
               '[clang-diagnostic-thread-safety-negative]', \
               '[clang-diagnostic-thread-safety-precise]', \
               '[clang-diagnostic-thread-safety-reference]', \
               '[clang-diagnostic-thread-safety-verbose]', \
               '[clang-diagnostic-trigraphs]', \
               '[clang-diagnostic-type-limits]', \
               '[clang-diagnostic-type-safety]', \
               '[clang-diagnostic-typedef-redefinition]', \
               '[clang-diagnostic-typename-missing]', \
               '[clang-diagnostic-unable-to-open-stats-file]', \
               '[clang-diagnostic-unavailable-declarations]', \
               '[clang-diagnostic-undeclared-selector]', \
               '[clang-diagnostic-undef]', \
               '[clang-diagnostic-undefined-bool-conversion]', \
               '[clang-diagnostic-undefined-func-template]', \
               '[clang-diagnostic-undefined-inline]', \
               '[clang-diagnostic-undefined-internal]', \
               '[clang-diagnostic-undefined-internal-type]', \
               '[clang-diagnostic-undefined-reinterpret-cast]', \
               '[clang-diagnostic-undefined-var-template]', \
               '[clang-diagnostic-unevaluated-expression]', \
               '[clang-diagnostic-unguarded-availability]', \
               '[clang-diagnostic-unguarded-availability-new]', \
               '[clang-diagnostic-unicode]', \
               '[clang-diagnostic-unicode-whitespace]', \
               '[clang-diagnostic-uninitialized]', \
               '[clang-diagnostic-unknown-argument]', \
               '[clang-diagnostic-unknown-attributes]', \
               '[clang-diagnostic-unknown-escape-sequence]', \
               '[clang-diagnostic-unknown-pragmas]', \
               '[clang-diagnostic-unknown-sanitizers]', \
               '[clang-diagnostic-unknown-warning-option]', \
               '[clang-diagnostic-unnamed-type-template-args]', \
               '[clang-diagnostic-unneeded-internal-declaration]', \
               '[clang-diagnostic-unneeded-member-function]', \
               '[clang-diagnostic-unreachable-code]', \
               '[clang-diagnostic-unreachable-code-aggressive]', \
               '[clang-diagnostic-unreachable-code-break;]', \
               '[clang-diagnostic-unreachable-code-loop-increment]', \
               '[clang-diagnostic-unreachable-code-return]', \
               '[clang-diagnostic-unsequenced]', \
               '[clang-diagnostic-unsupported-abs]', \
               '[clang-diagnostic-unsupported-availability-guard]', \
               '[clang-diagnostic-unsupported-cb]', \
               '[clang-diagnostic-unsupported-dll-base-class-template]', \
               '[clang-diagnostic-unsupported-friend]', \
               '[clang-diagnostic-unsupported-gpopt]', \
               '[clang-diagnostic-unsupported-nan]', \
               '[clang-diagnostic-unsupported-visibility]', \
               '[clang-diagnostic-unusable-partial-specialization]', \
               '[clang-diagnostic-unused-argument]', \
               '[clang-diagnostic-unused-command-line-argument]', \
               '[clang-diagnostic-unused-comparison]', \
               '[clang-diagnostic-unused-const-variable]', \
               '[clang-diagnostic-unused-exception-parameter]', \
               '[clang-diagnostic-unused-function]', \
               '[clang-diagnostic-unused-getter-return-value]', \
               '[clang-diagnostic-unused-label]', \
               '[clang-diagnostic-unused-lambda-capture]', \
               '[clang-diagnostic-unused-local-typedef]', \
               '[clang-diagnostic-unused-local-typedefs]', \
               '[clang-diagnostic-unused-macros]', \
               '[clang-diagnostic-unused-member-function]', \
               '[clang-diagnostic-unused-parameter]', \
               '[clang-diagnostic-unused-private-field]', \
               '[clang-diagnostic-unused-property-ivar]', \
               '[clang-diagnostic-unused-result]', \
               '[clang-diagnostic-unused-template]', \
               '[clang-diagnostic-unused-value]', \
               '[clang-diagnostic-unused-variable]', \
               '[clang-diagnostic-unused-volatile-lvalue]', \
               '[clang-diagnostic-used-but-marked-unused]', \
               '[clang-diagnostic-user-defined-literals]', \
               '[clang-diagnostic-user-defined-warnings]', \
               '[clang-diagnostic-varargs]', \
               '[clang-diagnostic-variadic-macros]', \
               '[clang-diagnostic-vec-elem-size]', \
               '[clang-diagnostic-vector-conversion]', \
               '[clang-diagnostic-vector-conversions]', \
               '[clang-diagnostic-vexing-parse]', \
               '[clang-diagnostic-visibility]', \
               '[clang-diagnostic-vla]', \
               '[clang-diagnostic-vla-extension]', \
               '[clang-diagnostic-void-ptr-dereference]', \
               '[clang-diagnostic-volatile-register-var]', \
               '[clang-diagnostic-weak-template-vtables]', \
               '[clang-diagnostic-weak-vtables]', \
               '[clang-diagnostic-writable-strings]', \
               '[clang-diagnostic-write-strings]', \
               '[clang-diagnostic-zero-as-null-pointer-constant]', \
               '[clang-diagnostic-zero-length-array]'
               ]


class checks:
    def __init__(self, dataval=None):
        self.name = ''
        self.count = 0
        self.data = ''


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--button', action='store_true')
    parser.add_argument('file', type=argparse.FileType('r'))

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        usage()
        sys.exit()

    external_link = ''
    external_name = ''
    if (args.button):
        external_link = input("What is the full link address?\n")
        external_name = input("What would you like to name this link?\n")

    contents = args.file.readlines()
    checks_list.sort()
    checks_used = [0] * 1000
    # Increments each occurrence of a check.
    for line, content in enumerate(contents):
        content = content.replace('<', '&lt;')
        content = content.replace('>', '&gt;')
        for check_name in checks_list:
            if content.find(check_name) != -1:
                checks_used[checks_list.index(check_name)] += 1

    # Counts the max number of used checks in the log file.
    num_used_checks = 0
    for line, check in enumerate(checks_list):
        if checks_used[line] != 0:
            num_used_checks += 1

    names_of_used = [None] * num_used_checks
    names_of_usedL = [None] * num_used_checks

    # Creates new check classes for each used check.
    used_line = 0
    total_num_checks = 0
    for line, check in enumerate(checks_list):
        if checks_used[line] != 0:
            new_node = checks(check)
            new_node.name = check
            new_node.count = checks_used[line]
            total_num_checks += checks_used[line]
            names_of_used[used_line] = new_node

            names_of_usedL[used_line] = checks_list[line]
            used_line += 1

    # Adds details for each organized check.
    for line, content in enumerate(contents):
        for initial_check in names_of_usedL:
            if content.find(initial_check) != -1:
                names_of_used[names_of_usedL.index(
                    initial_check)].data += content
                details = line + 1
                finished = False
                while not finished:
                    if details >= len(contents):
                        break
                    for end_check in names_of_usedL:
                        if contents[details].find(end_check) != -1:
                            finished = True
                            break
                    if not finished:
                        names_of_used[names_of_usedL.index(
                            initial_check)].data += contents[details]
                        details += 1

    args.file.close()
    f = open("clang.html", "w")

    writeHeader(f)
    writeList(f, num_used_checks, names_of_used, args,
              external_link, external_name, total_num_checks)
    sortLogs(f, contents, num_used_checks, names_of_used,
             args, external_link, external_name)
    writeScript(f, num_used_checks)
    f.close()
    sys.exit()


def usage():
    print("**--------------------------- Clang Visualizer --------------------------**\n\n \
    Generates an html file as a visual for clang-tidy checks.\n\n \
    Arguments: python clang_visualizer.py [logfile.log]\n\n \
    Options:\n\t\t'-b', '--button': External link button for the html page.\n \
    \t\t-Prompts the user for a hyperlink and name.\n \
    \t\t-ex: python clang_visualizer -b [logfile.log] \
    \n\n**------------------------------------------------------------------------**")


def writeHeader(f):
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("\t<title>Clang-Tidy Visualizer</title>\n\t<meta charset=\"UTF-8\">\n")
    f.write("\t<meta name=\"author\" content=\"Austin Hale\">\n")
    f.write("\t<meta name=\"description\" content=\"Documentation tool for visualizing Clang-Tidy checks.\">\n")
    f.write(
        "\t<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n")
    f.write("\t<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">\n")
    f.write("\t<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>\n")
    f.write("\t<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js\"></script>\n")
    f.write("</head>\n")


def writeList(f, num_used_checks, names_of_used, args, external_link, external_name, total_num_checks):
    f.write(
        "<body style=\"background: rgb(220, 227, 230); width: 100%; height: 100%;\">\n")
    f.write("<div id=\"container\" style=\"margin-left: 2%; margin-right: 2%;\">\n")
    f.write("\t<div id=\"header\" style=\"height: 55px; display: flex; justify-content: left; position: relative;\">\n")
    f.write("\t\t<h3 style=\"text-align: center; color: #111; font-family: 'Helvetica Neue', sans-serif; font-weight: bold; \
    letter-spacing: 0.5px; line-height: 1;\">Clang-Tidy Checks</h3>\n")
    f.write("\t\t<div class=\"btn-group\" role=\"group\" style=\"position: absolute; right: 0;\">\n")
    f.write("\t\t\t<button type=\"button\" class=\"btn btn-warning\" onclick=\"highlightChecks(0)\" style=\"outline: none; color: black\">Warning</button>\n")
    f.write("\t\t\t<button type=\"button\" class=\"btn btn-danger\" onclick=\"highlightChecks(1)\" style=\"outline: none; color: black\">Danger</button>\n")
    f.write("\t\t\t<button type=\"button\" class=\"btn btn-info\" onclick=\"clearChecks()\" style=\"outline: none; color: black\">Clear All</button>\n")
    f.write("\t\t</div>\n\t</div><br>\n")
    f.write("\t<ul id=\"list\" class=\"list-group\" align=\"left\" style=\"display: block; width: 25%; height: 0; margin-bottom: 0;\">\n")

    # Iterates through each used check's details and organizes them into the given <pre> sections.
    f.write("\t\t<a id=\"log\" href=\"#\" class=\"list-group-item list-group-item-success\" style=\"color: black; font-weight: bold; letter-spacing:0.4px;\" \
    onclick=\"toggleLog()\">%d Original Log</a>\n" % (total_num_checks))

    for line in range(0, num_used_checks):
        f.write("\t\t<a id=\"check%d\" style=\"color: black\" href=\"#\" class=\"list-group-item list-group-item-action\" \
        onclick=\"toggleInfo(%d)\">%d %s</a>\n" % (line, line, names_of_used[line].count, names_of_used[line].name))

    f.write("\t</ul>\n\n")
    f.write(
        "\t<div id=\"showLog\" style=\"display: none; width: 75%; float: right;\">\n")
    f.write(
        "\t\t<div style=\"display: flex; justify-content: left; position: relative;\">\n")
    f.write("\t\t\t<button id=\"collapse-btn0\" type=\"button\" class=\"btn nohover\" onclick=\"collapseSidebar()\" style=\"outline: none; \
    background-color: lightgray\" title=\"Collapse sidebar\">\n")
    f.write("\t\t\t<span id=\"collapse-img0\" class=\"glyphicon glyphicon-menu-left\"></button></span>\n")
    f.write("\t\t\t<h4 style=\"margin-top: 0; color: #111; position: absolute; left: 50%; transform: translateX(-50%); margin-bottom: 10;\">Original Log</h4>\n")
    if (args.button):
        f.write("\t\t\t<button id=\"externalLink\" type=\"button\" class=\"btn\" onclick=\"window.open('%s','_blank')\"\n" % external_link)
        f.write("\t\t\tstyle=\"outline: none; position: absolute; color: #111; right: 0; background-color: rgb(181, 215, 247)\">\n")
        f.write(
            "\t\t\t%s <span class=\"glyphicon glyphicon-new-window\"></button></span>\n" % external_name)

    f.write("\t\t</div>\n\t\t<pre>\n")


def sortLogs(f, contents, num_used_checks, names_of_used, args, external_link, external_name):
    for line in contents:
        f.write("%s" % (line))

    f.write("\n\t\t</pre>\n\t</div>\n")

    for check_idx in range(0, num_used_checks):
        collapse_idx = check_idx+1
        f.write("\t<div id=\"show%d\"" % (check_idx))
        f.write("style=\"display: none; width: 75%; float: right\">\n")
        f.write(
            "\t\t<div style=\"display: flex; justify-content: left; position: relative;\">\n")
        f.write("\t\t\t<button id=\"collapse-btn%d\" type=\"button\" class=\"btn nohover\" onclick=\"collapseSidebar()\" \
        style=\"outline: none; background-color: lightgray\" title=\"Collapse sidebar\">\n" % (collapse_idx))
        f.write("\t\t\t<span id=\"collapse-img%d\" class=\"glyphicon glyphicon-menu-left\"></button></span>\n" % (collapse_idx))
        f.write("\t\t\t<h4 style=\"margin-top: 0; color: #111; position: absolute; left: 50%; transform: translateX(-50%); margin-bottom: 10\">")
        f.write("%s</h4>\n" % (names_of_used[check_idx].name[1:-1]))
        if (args.button):
            f.write("\t\t\t<button id=\"externalLink\" type=\"button\" class=\"btn\" onclick=\"window.open('%s','_blank')\"\n" % external_link)
            f.write("\t\t\tstyle=\"outline: none; position: absolute; color: #111; right: 0; background-color: rgb(181, 215, 247)\">\n")
            f.write(
                "\t\t\t%s <span class=\"glyphicon glyphicon-new-window\"></button></span>\n" % external_name)
        f.write("\t\t</div>\n\t\t<pre>\n")
        f.write("%s\t\t</pre>\n\t</div>\n" % (names_of_used[check_idx].data))

    f.write("</div>\n</body>\n")

# Writes Javascript and JQuery code to the html file for button and grouping functionalities.


def writeScript(f, num_used_checks):
    f.write("<script>\nvar selected_idx;\nvar checks_arr = [];\nvar highlights = 'highlights';\n")
    f.write("// Retrieves local storage data on document load for highlighted checks.\n")
    f.write(
        "$(document).ready(function() {\n\tfor (var all_checks=0; all_checks<%d; all_checks++) {\n" % (num_used_checks))
    f.write("\t\tvar check_hl = document.getElementById(\"check\"+all_checks);\n")
    f.write(
        "\t\tswitch (JSON.parse(localStorage.getItem(highlights))[all_checks]) {\n")
    f.write("\t\t\tcase \"warning\":\n\t\t\tcheck_hl.classList.add('list-group-item-warning');\n")
    f.write(
        "\t\t\tchecks_arr[all_checks] = \"warning\"; break;\n\t\t\tcase \"danger\":\n")
    f.write(
        "\t\t\tcheck_hl.classList.add('list-group-item-danger');\n\t\t\tchecks_arr[all_checks] = \"danger\"; break;\n")
    f.write(
        "\t\t\tdefault:\n\t\t\tchecks_arr[all_checks] = \"action\";\n\t\t\tif (check_hl !== null) {\n")
    f.write("\t\t\t\tcheck_hl.classList.add('list-group-item-action');\n\t\t\t} break;\n\t\t}\n\t}\n")
    f.write("localStorage.setItem(highlights, JSON.stringify(checks_arr));\n});\n\n")

    f.write(
        "function toggleLog() {\n\tvar log = document.getElementById(\"showLog\");\n\tclearContent();\n")
    f.write(
        "\tif (log.style.display === \"none\") {\n\t\tlog.style.display = \"block\";\n\t} else {\n")
    f.write("\t\tlog.style.display = \"none\";\n\t}\n}\n\n")

    f.write(
        "function toggleInfo(check_position) {\n\tselected_idx = check_position;\n\tclearContent();\n")
    f.write("\t// Displays the chosen clang-tidy category.\n\tvar category = document.getElementById(\"show\"+check_position);\n")
    f.write(
        "\tif (category.style.display === \"none\") {\n\t\tcategory.style.display = \"block\";\n\t} else {\n")
    f.write("\t\tcategory.style.display = \"none\";\n\t}\n}\n\n")

    f.write(
        "// Clears document when choosing another selection.\nfunction clearContent() {\n")
    f.write(
        "\tfor (var all_checks=0; all_checks<%d; all_checks++) {\n\t\tvar clear = document.getElementById(\"show\"+all_checks);\n" % (num_used_checks))
    f.write(
        "\t\tif (clear.style.display === \"block\") {\n\t\tclear.style.display = \"none\";\n\t\t}\n\t}\n")
    f.write(
        "\tvar clearLog = document.getElementById(\"showLog\");\n\tif (clearLog.style.display === \"block\") {\n")
    f.write("\t\tclearLog.style.display = \"none\";\n\t}\n}\n\n")

    f.write(
        "// Type 1 used for highlighting danger checks and 0 for warnings.\nfunction highlightChecks(type) {\n")
    f.write(
        "\tvar check_hl = document.getElementById(\"check\"+selected_idx);\n\tif (check_hl !== null) {\n")
    f.write(
        "\t\tif (check_hl.classList.contains('list-group-item-action')) {\n\t\t\tcheck_hl.classList.remove('list-group-item-action');\n")
    f.write("\t\t\ttype == 1 ? check_hl.classList.add('list-group-item-danger') : check_hl.classList.add('list-group-item-warning');\n")
    f.write(
        "\t\t\ttype == 1 ? checks_arr[selected_idx] = \"danger\" : checks_arr[selected_idx] = \"warning\";\n")
    f.write(
        "\t\t} else if (check_hl.classList.contains('list-group-item-warning')) {\n\t\t\tcheck_hl.classList.remove('list-group-item-warning');\n")
    f.write("\t\t\ttype == 1 ? check_hl.classList.add('list-group-item-danger') : check_hl.classList.add('list-group-item-action');\n")
    f.write(
        "\t\t\ttype == 1 ? checks_arr[selected_idx] = \"danger\" : checks_arr[selected_idx] = \"action\";\n\t\t} else {\n")
    f.write("\t\t\tcheck_hl.classList.remove('list-group-item-danger');\n")
    f.write("\t\t\ttype == 1 ? check_hl.classList.add('list-group-item-action') : check_hl.classList.add('list-group-item-warning');\n")
    f.write(
        "\t\t\ttype == 1 ? checks_arr[selected_idx] = \"action\" : checks_arr[selected_idx] = \"warning\";\n\t\t}\n\t}\n")
    f.write("\t// Sets local storage for each occurrence of a highlighted check.\n\tlocalStorage.setItem(highlights, JSON.stringify(checks_arr));\n}\n\n")

    f.write(
        "function clearChecks(type) {\n\tfor (var all_checks=0; all_checks<%d; all_checks++) {\n" % (num_used_checks))
    f.write(
        "\t\tvar clear = (document.getElementById(\"check\"+all_checks));\n\t\tchecks_arr[all_checks] = \"action\";\n")
    f.write("\t\tif (clear !== null) {\n")
    f.write(
        "\t\t\tif (clear.classList.contains('list-group-item-warning')) {\n\t\t\t\tclear.classList.remove('list-group-item-warning');\n")
    f.write(
        "\t\t\t} else if (clear.classList.contains('list-group-item-danger')) {\n\t\t\t\tclear.classList.remove('list-group-item-danger');\n\t\t\t}\n")
    f.write("\t\t\tclear.classList.add('list-group-item-action');\n\t\t}\n\t}\n\t// Restores all checks to unhighlighted state on local storage.\n")
    f.write("\tlocalStorage.removeItem(highlights);\n}\n\n")

    f.write(
        "function collapseSidebar() {\n\tvar list = document.getElementById(\"list\"); var hasExpanded;\n")
    f.write("\tvar log_details = document.getElementById(\"showLog\");\n\tlist.style.display === \"block\" ? hasSidebar = true : hasSidebar = false;\n")
    f.write(
        "\thasSidebar ? list.style.display = \"none\" : list.style.display = \"block\";\n")
    f.write(
        "\tfor (var all_checks=0; all_checks<=%d; all_checks++) {\n\t\tvar collapse_img = document.getElementById(\"collapse-img\"+all_checks);\n" % (num_used_checks))
    f.write("\t\tvar collapse_btn = document.getElementById(\"collapse-btn\"+all_checks);\n\t\tvar check_details = document.getElementById(\"show\"+all_checks);\n")
    f.write(
        "\t\tif (collapse_img !== null) {\n\t\t\thasSidebar ? collapse_img.classList.remove('glyphicon-menu-left') : collapse_img.classList.remove('glyphicon-menu-right');\n")
    f.write("\t\t\thasSidebar ? collapse_img.classList.add('glyphicon-menu-right') : collapse_img.classList.add('glyphicon-menu-left');\n")
    f.write("\t\t\thasSidebar ? collapse_btn.title = \"Expand sidebar\" : collapse_btn.title = \"Collapse sidebar\";\n\t\t}\n")
    f.write(
        "\t\tif (check_details !== null) {hasSidebar ? check_details.style.width = \"100%\" : check_details.style.width = \"75%\";}\n\t}\n")
    f.write("\thasSidebar ? log_details.style.width = \"100%\" : log_details.style.width = \"75%\";\n}\n")

    # Begins writing style elements.
    f.write("</script>\n<style>\n\tpre {\n\t\twhite-space: pre-wrap;\n")
    f.write("\t\tword-break: keep-all;\n\t}\n\t#header {\n")
    f.write("\t\tborder-bottom: 2px solid darkgray\n\t}\n")
    f.write("</style>\n</html>")


# Calls main function.
if __name__ == "__main__":
    main()
