# Program compilation with g++

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Compile and run a C++ program using the g++ compiler from the command line.

## Compilation Commands
```bash
# Basic compilation
g++ main.cpp -o myprogram
./myprogram

# With C++17 standard
g++ -std=c++17 main.cpp -o myprogram

# With warnings enabled (ALWAYS do this)
g++ -std=c++17 -Wall -Wextra main.cpp -o myprogram

# With debugging info (for gdb)
g++ -std=c++17 -Wall -g main.cpp -o myprogram

# With optimization
g++ -std=c++17 -O2 main.cpp -o myprogram

# With address sanitizer (find memory bugs)
g++ -std=c++17 -Wall -fsanitize=address -g main.cpp -o myprogram

# Multiple source files
g++ -std=c++17 main.cpp utils.cpp math.cpp -o myprogram
```

## Compilation Steps (What g++ Does)
```
1. Preprocessing:  g++ -E main.cpp    → Expands #include, #define
2. Compilation:    g++ -S main.cpp    → Generates assembly (.s file)
3. Assembly:       g++ -c main.cpp    → Generates object file (.o)
4. Linking:        g++ main.o -o prog → Links object files into executable
```

## Key Flags
| Flag | Purpose |
|------|---------|
| `-std=c++17` | Use C++17 standard |
| `-Wall` | Enable common warnings |
| `-Wextra` | Enable extra warnings |
| `-g` | Include debug info |
| `-O0` / `-O2` / `-O3` | Optimization levels |
| `-fsanitize=address` | Detect memory errors |
| `-fsanitize=undefined` | Detect undefined behavior |

## Key Takeaways
1. Always compile with `-Wall -Wextra`
2. Use `-std=c++17` (or c++20) for modern features
3. Use `-g` when debugging with gdb
4. Use `-fsanitize=address` to catch memory bugs


g++ --help
Usage: g++ [options] file...
Options:
  -pass-exit-codes         Exit with highest error code from a phase.
  --help                   Display this information.
  --target-help            Display target specific command line options.
  --help={common|optimizers|params|target|warnings|[^]{joined|separate|undocumented}}[,...].
                           Display specific types of command line options.
  (Use '-v --help' to display command line options of sub-processes).
  --version                Display compiler version information.
  -dumpspecs               Display all of the built in spec strings.
  -dumpversion             Display the version of the compiler.
  -dumpmachine             Display the compiler's target processor.
  -print-search-dirs       Display the directories in the compiler's search path.
  -print-libgcc-file-name  Display the name of the compiler's companion library.
  -print-file-name=<lib>   Display the full path to library <lib>.
  -print-prog-name=<prog>  Display the full path to compiler component <prog>.
  -print-multiarch         Display the target's normalized GNU triplet, used as
                           a component in the library path.
  -print-multi-directory   Display the root directory for versions of libgcc.
  -print-multi-lib         Display the mapping between command line options and
                           multiple library search directories.
  -print-multi-os-directory Display the relative path to OS libraries.
  -print-sysroot           Display the target libraries directory.
  -print-sysroot-headers-suffix Display the sysroot suffix used to find headers.
  -Wa,<options>            Pass comma-separated <options> on to the assembler.
  -Wp,<options>            Pass comma-separated <options> on to the preprocessor.
  -Wl,<options>            Pass comma-separated <options> on to the linker.
  -Xassembler <arg>        Pass <arg> on to the assembler.
  -Xpreprocessor <arg>     Pass <arg> on to the preprocessor.
  -Xlinker <arg>           Pass <arg> on to the linker.
  -save-temps              Do not delete intermediate files.
  -save-temps=<arg>        Do not delete intermediate files.
  -no-canonical-prefixes   Do not canonicalize paths when building relative
                           prefixes to other gcc components.
  -pipe                    Use pipes rather than intermediate files.
  -time                    Time the execution of each subprocess.
  -specs=<file>            Override built-in specs with the contents of <file>.
  -std=<standard>          Assume that the input sources are for <standard>.
  --sysroot=<directory>    Use <directory> as the root directory for headers
                           and libraries.
  -B <directory>           Add <directory> to the compiler's search paths.
  -v                       Display the programs invoked by the compiler.
  -###                     Like -v but options quoted and commands not executed.
  -E                       Preprocess only; do not compile, assemble or link.
  -S                       Compile only; do not assemble or link.
  -c                       Compile and assemble, but do not link.
  -o <file>                Place the output into <file>.
  -pie                     Create a dynamically linked position independent
                           executable.
  -shared                  Create a shared library.
  -x <language>            Specify the language of the following input files.
                           Permissible languages include: c c++ assembler none
                           'none' means revert to the default behavior of
                           guessing the language based on the file's extension.

Options starting with -g, -f, -m, -O, -W, or --param are automatically
 passed on to the various sub-processes invoked by g++.  In order to pass
 other options on to these processes the -W<letter> options must be used.

For bug reporting instructions, please see:
<file:///usr/share/doc/gcc-11/README.Bugs>.
23u58g@tcidev03:~/work/viswa_local/general$ 

## Viswa additional 
 g++ -fsanitize
-fsanitize=                                   -fsanitize=null                               -fsanitize-recover=integer-divide-by-zero     -fsanitize-recover=unreachable
-fsanitize=address                            -fsanitize=object-size                        -fsanitize-recover=kernel-address             -fsanitize-recover=vla-bound
-fsanitize-address-use-after-scope            -fsanitize=pointer-compare                    -fsanitize-recover=kernel-hwaddress           -fsanitize-recover=vptr
-fsanitize=alignment                          -fsanitize=pointer-overflow                   -fsanitize-recover=leak                       -fsanitize=return
-fsanitize=bool                               -fsanitize=pointer-subtract                   -fsanitize-recover=nonnull-attribute          -fsanitize=returns-nonnull-attribute
-fsanitize=bounds                             -fsanitize-recover                            -fsanitize-recover=null                       -fsanitize-sections=
-fsanitize=bounds-strict                      -fsanitize-recover=                           -fsanitize-recover=object-size                -fsanitize=shift
-fsanitize=builtin                            -fsanitize-recover=address                    -fsanitize-recover=pointer-compare            -fsanitize=shift-base
-fsanitize-coverage=                          -fsanitize-recover=alignment                  -fsanitize-recover=pointer-overflow           -fsanitize=shift-exponent
-fsanitize=enum                               -fsanitize-recover=all                        -fsanitize-recover=pointer-subtract           -fsanitize=signed-integer-overflow
-fsanitize=float-cast-overflow                -fsanitize-recover=bool                       -fsanitize-recover=return                     -fsanitize=thread
-fsanitize=float-divide-by-zero               -fsanitize-recover=bounds                     -fsanitize-recover=returns-nonnull-attribute  -fsanitize=undefined


g++ -std
-std=c++03           -std=c18             -std=c++2b           -std=f2003           -std=gnu++0x         -std=gnu1x           -std=gnu2x           -std=iso9899:199409  -stdlib=
-std=c++0x           -std=c1x             -std=c2x             -std=f2008           -std=gnu++11         -std=gnu++1y         -std=gnu89           -std=iso9899:1999    -stdlib=libc++
-std=c++11           -std=c++1y           -std=c89             -std=f2008ts         -std=gnu11           -std=gnu++1z         -std=gnu90           -std=iso9899:199x    -stdlib=libstdc++
-std=c11             -std=c++1z           -std=c90             -std=f2018           -std=gnu++14         -std=gnu++20         -std=gnu++98         -std=iso9899:2011    
-std=c++14           -std=c++20           -std=c++98           -std=f95             -std=gnu++17         -std=gnu++23         -std=gnu99           -std=iso9899:2017    
-std=c++17           -std=c++23           -std=c99             -std=gnu             -std=gnu17           -std=gnu++2a         -std=gnu9x           -std=iso9899:2018    
-std=c17             -std=c++2a           -std=c9x             -std=gnu++03         -std=gnu18           -std=gnu++2b         -std=iso9899:1990    -std=legacy    


 g++ -O
-O      -Ofast  -Og     -Os   


g++ -W
Display all 755 possibilities? (y or n)
-W                                                 -Wno-analyzer-use-after-free                       -Wno-sign-conversion
-Wa,                                               -Wno-analyzer-use-of-pointer-in-stale-stack-frame  -Wno-sign-promo
-Wabi                                              -Wno-analyzer-write-to-const                       -Wno-sized-deallocation
-Wabi=                                             -Wno-analyzer-write-to-string-literal              -Wno-sizeof-array-argument
-Wabi-tag                                          -Wno-argument-mismatch                             -Wno-sizeof-array-div
-Wabsolute-value                                   -Wno-arith-conversion                              -Wno-sizeof-pointer-div
-Waddress                                          -Wno-array-bounds                                  -Wno-sizeof-pointer-memaccess
-Waddress-of-packed-member                         -Wno-array-parameter                               -Wno-speculative
-Waggregate-return                                 -Wno-array-temporaries                             -Wno-stack-protector
-Waggressive-loop-optimizations                    -Wno-assign-intercept                              -Wno-stack-usage
-Waliasing                                         -Wno-attribute-alias                               -Wno-strict-aliasing
-Walign-commons                                    -Wno-attributes                                    -Wno-strict-null-sentinel
-Waligned-new                                      -Wno-attribute-warning                             -Wno-strict-overflow
-Waligned-new=                                     -Wno-bad-function-cast                             -Wno-strict-prototypes
-Waligned-new=all                                  -Wno-bool-compare                                  -Wno-strict-selector-match
-Waligned-new=global                               -Wno-bool-operation                                -Wno-string-compare
-Waligned-new=none                                 -Wno-builtin-declaration-mismatch                  -Wno-stringop-overflow
-Wall                                              -Wno-builtin-macro-redefined                       -Wno-stringop-overread
-Walloca                                           -Wno-c++0x-compat                                  -Wno-stringop-truncation
-Walloca-larger-than=                              -Wno-c11-c2x-compat                                -Wno-students
-Walloc-size-larger-than=                          -Wno-c++11-compat                                  -Wno-subobject-linkage
-Walloc-zero                                       -Wno-c++14-compat                                  -Wno-suggest-attribute=cold
-Wampersand                                        -Wno-c++17-compat                                  -Wno-suggest-attribute=const
-Wanalyzer-double-fclose                           -Wno-c++1z-compat                                  -Wno-suggest-attribute=format
-Wanalyzer-double-free                             -Wno-c++20-compat                                  -Wno-suggest-attribute=malloc
-Wanalyzer-exposure-through-output-file            -Wno-c++2a-compat                                  -Wno-suggest-attribute=noreturn
-Wanalyzer-file-leak                               -Wno-c90-c99-compat                                -Wno-suggest-attribute=pure
-Wanalyzer-free-of-non-heap                        -Wno-c99-c11-compat                                -Wno-suggest-final-methods
-Wanalyzer-malloc-leak                             -Wno-cannot-profile                                -Wno-suggest-final-types
-Wanalyzer-mismatching-deallocation                -Wno-cast-align                                    -Wno-suggest-override
-Wanalyzer-null-argument                           -Wno-cast-align=strict                             -Wno-surprising
-Wanalyzer-null-dereference                        -Wno-cast-function-type                            -Wno-switch
-Wanalyzer-possible-null-argument                  -Wno-cast-qual                                     -Wno-switch-bool
-Wanalyzer-possible-null-dereference               -Wno-cast-result                                   -Wno-switch-default
-Wanalyzer-shift-count-negative                    -Wno-catch-value                                   -Wno-switch-enum
-Wanalyzer-shift-count-overflow                    -Wno-c-binding-type                                -Wno-switch-outside-range
-Wanalyzer-stale-setjmp-buffer                     -Wno-c++-compat                                    -Wno-switch-unreachable
-Wanalyzer-tainted-array-index                     -Wno-character-truncation                          -Wno-sync-nand
-Wanalyzer-too-complex                             -Wno-char-subscripts                               -Wno-synth
-Wanalyzer-unsafe-call-within-signal-handler       -Wno-chkp                                          -Wno-system-headers
-Wanalyzer-use-after-free                          -Wno-class-conversion                              -Wno-tabs
-Wanalyzer-use-of-pointer-in-stale-stack-frame     -Wno-class-memaccess                               -Wno-target-lifetime
-Wanalyzer-write-to-const                          -Wno-clobbered                                     -Wno-tautological-compare
-Wanalyzer-write-to-string-literal                 -Wno-comma-subscript                               -Wno-templates
-Wargument-mismatch                                -Wno-comment                                       -Wno-terminate
-Warith-conversion                                 -Wno-comments                                      -Wno-traditional
-Warray-bounds                                     -Wno-compare-reals                                 -Wno-traditional-conversion
-Warray-bounds=                                    -Wno-conditionally-supported                       -Wno-trampolines
-Warray-parameter                                  -Wno-conversion                                    -Wno-trigraphs
-Warray-parameter=                                 -Wno-conversion-extra                              -Wno-tsan
-Warray-temporaries                                -Wno-conversion-null                               -Wno-type-limits
-Wassign-intercept                                 -Wno-coverage-mismatch                             -Wno-undeclared-selector
-Wattribute-alias                                  -Wno-cpp                                           -Wno-undef
-Wattribute-alias=                                 -Wno-ctad-maybe-unsupported                        -Wno-undefined-do-loop
-Wattributes                                       -Wno-ctor-dtor-privacy                             -Wno-underflow
-Wattribute-warning                                -Wno-dangling-else                                 -Wno-uninitialized
-Wbad-function-cast                                -Wno-date-time                                     -Wno-unknown-pragmas
-Wbool-compare                                     -Wno-declaration-after-statement                   -Wno-unreachable-code
-Wbool-operation                                   -Wno-delete-incomplete                             -Wno-unsafe-loop-optimizations
-Wbuiltin-declaration-mismatch                     -Wno-delete-non-virtual-dtor                       -Wno-unsuffixed-float-constants
-Wbuiltin-macro-redefined                          -Wno-deprecated                                    -Wno-unused
-Wc++0x-compat                                     -Wno-deprecated-copy                               -Wno-unused-but-set-parameter
-Wc11-c2x-compat                                   -Wno-deprecated-copy-dtor                          -Wno-unused-but-set-variable
-Wc++11-compat                                     -Wno-deprecated-declarations                       -Wno-unused-const-variable
-Wc++14-compat                                     -Wno-deprecated-enum-enum-conversion               -Wno-unused-dummy-argument
-Wc++17-compat                                     -Wno-deprecated-enum-float-conversion              -Wno-unused-function
-Wc++1z-compat                                     -Wno-designated-init                               -Wno-unused-label
-Wc++20-compat                                     -Wno-disabled-optimization                         -Wno-unused-local-typedefs
-Wc++2a-compat                                     -Wno-discarded-array-qualifiers                    -Wno-unused-macros
-Wc90-c99-compat                                   -Wno-discarded-qualifiers                          -Wno-unused-parameter
-Wc99-c11-compat                                   -Wno-div-by-zero                                   -Wno-unused-result
-Wcannot-profile                                   -Wno-do-subscript                                  -Wno-unused-value
-Wcast-align                                       -Wno-double-promotion                              -Wno-unused-variable
-Wcast-align=strict                                -Wno-duplicated-branches                           -Wno-useless-cast
-Wcast-function-type                               -Wno-duplicated-cond                               -Wno-use-without-only
-Wcast-qual                                        -Wno-duplicate-decl-specifier                      -Wno-varargs
-Wcast-result                                      -Wno-effc++                                        -Wno-variadic-macros
-Wcatch-value                                      -Wno-empty-body                                    -Wno-vector-operation-performance
-Wcatch-value=                                     -Wno-endif-labels                                  -Wno-verbose-unbounded
-Wc-binding-type                                   -Wno-enum-compare                                  -Wno-vexing-parse
-Wc++-compat                                       -Wno-enum-conversion                               -Wno-virtual-inheritance
-Wcharacter-truncation                             -Wno-error                                         -Wno-virtual-move-assign
-Wchar-subscripts                                  -Wno-error=                                        -Wno-vla
-Wchkp                                             -Wnoexcept                                         -Wno-vla-larger-than
-Wclass-conversion                                 -Wno-exceptions                                    -Wno-vla-larger-than=
-Wclass-memaccess                                  -Wnoexcept-type                                    -Wno-vla-parameter
-Wclobbered                                        -Wno-expansion-to-defined                          -Wno-volatile
-Wcomma-subscript                                  -Wno-extra                                         -Wno-volatile-register-var
-Wcomment                                          -Wno-extra-semi                                    -Wno-write-strings
-Wcomments                                         -Wno-fatal-errors                                  -Wno-zero-as-null-pointer-constant
-Wcompare-reals                                    -Wno-float-conversion                              -Wno-zero-length-bounds
-Wconditionally-supported                          -Wno-float-equal                                   -Wno-zerotrip
-Wconversion                                       -Wno-format                                        -WNSObject-attribute
-Wconversion-extra                                 -Wno-format-contains-nul                           -Wnull-dereference
-Wconversion-null                                  -Wno-format-diag                                   -Wobjc-root-class
-Wcoverage-mismatch                                -Wno-format-extra-args                             -Wodr
-Wcpp                                              -Wno-format-nonliteral                             -Wold-style-cast
-Wctad-maybe-unsupported                           -Wno-format-overflow                               -Wold-style-declaration
-Wctor-dtor-privacy                                -Wno-format-security                               -Wold-style-definition
-Wdangling-else                                    -Wno-format-signedness                             -Wopenmp-simd
-Wdate-time                                        -Wno-format-truncation                             -Woverflow
-Wdeclaration-after-statement                      -Wno-format-y2k                                    -Woverlength-strings
-Wdelete-incomplete                                -Wno-format-zero-length                            -Woverloaded-virtual
-Wdelete-non-virtual-dtor                          -Wno-frame-address                                 -Woverride-init
-Wdeprecated                                       -Wno-frame-larger-than                             -Woverride-init-side-effects
-Wdeprecated-copy                                  -Wno-free-nonheap-object                           -Woverwrite-recursive
-Wdeprecated-copy-dtor                             -Wno-frontend-loop-interchange                     -Wp,
-Wdeprecated-declarations                          -Wno-function-elimination                          -Wpacked
-Wdeprecated-enum-enum-conversion                  -Wno-hsa                                           -Wpacked-bitfield-compat
-Wdeprecated-enum-float-conversion                 -Wno-if-not-aligned                                -Wpacked-not-aligned
-Wdesignated-init                                  -Wno-ignored-attributes                            -Wpadded
-Wdisabled-optimization                            -Wno-ignored-qualifiers                            -Wparentheses
-Wdiscarded-array-qualifiers                       -Wno-implicit                                      -Wpedantic
-Wdiscarded-qualifiers                             -Wno-implicit-fallthrough                          -Wpedantic-cast
-Wdiv-by-zero                                      -Wno-implicit-function-declaration                 -Wpedantic-param-names
-Wdo-subscript                                     -Wno-implicit-int                                  -Wpessimizing-move
-Wdouble-promotion                                 -Wno-implicit-interface                            -Wplacement-new
-Wduplicated-branches                              -Wno-implicit-procedure                            -Wplacement-new=
-Wduplicated-cond                                  -Wno-import                                        -Wpmf-conversions
-Wduplicate-decl-specifier                         -Wno-inaccessible-base                             -Wpointer-arith
-Weffc++                                           -Wno-incompatible-pointer-types                    -Wpointer-compare
-Wempty-body                                       -Wno-inherited-variadic-ctor                       -Wpointer-sign
-Wendif-labels                                     -Wno-init-list-lifetime                            -Wpointer-to-int-cast
-Wenum-compare                                     -Wno-init-self                                     -Wpragmas
-Wenum-conversion                                  -Wno-inline                                        -Wprio-ctor-dtor
-Werror                                            -Wno-int-conversion                                -Wproperty-assign-default
-Werror=                                           -Wno-integer-division                              -Wprotocol
-Werror-implicit-function-declaration              -Wno-int-in-bool-context                           -Wpsabi
-Wexceptions                                       -Wno-intrinsic-shadow                              -Wrange-loop-construct
-Wexpansion-to-defined                             -Wno-intrinsics-std                                -Wrealloc-lhs
-Wextra                                            -Wno-int-to-pointer-cast                           -Wrealloc-lhs-all
-Wextra-semi                                       -Wno-invalid-imported-macros                       -Wreal-q-constant
-Wfatal-errors                                     -Wno-invalid-memory-model                          -Wredundant-decls
-Wfloat-conversion                                 -Wno-invalid-offsetof                              -Wredundant-move
-Wfloat-equal                                      -Wno-invalid-pch                                   -Wredundant-tags
-Wformat                                           -Wno-jump-misses-init                              -Wregister
-Wformat=                                          -Wno-larger-than                                   -Wreorder
-Wformat-contains-nul                              -Wno-line-truncation                               -Wrestrict
-Wformat-diag                                      -Wno-literal-suffix                                -Wreturn-local-addr
-Wformat-extra-args                                -Wno-logical-not-parentheses                       -Wreturn-type
-Wformat-nonliteral                                -Wno-logical-op                                    -Wscalar-storage-order
-Wformat-overflow                                  -Wno-long-long                                     -Wselector
-Wformat-overflow=                                 -Wno-lto-type-mismatch                             -Wsequence-point
-Wformat-security                                  -Wno-main                                          -Wshadow
-Wformat-signedness                                -Wno-maybe-uninitialized                           -Wshadow-compatible-local
-Wformat-truncation                                -Wno-memset-elt-size                               -Wshadow=compatible-local
-Wformat-truncation=                               -Wno-memset-transposed-args                        -Wshadow=global
-Wformat-y2k                                       -Wno-misleading-indentation                        -Wshadow-ivar
-Wformat-zero-length                               -Wno-mismatched-dealloc                            -Wshadow-local
-Wframe-address                                    -Wno-mismatched-new-delete                         -Wshadow=local
-Wframe-larger-than=                               -Wno-mismatched-tags                               -Wshift-count-negative
-Wfree-nonheap-object                              -Wno-missing-attributes                            -Wshift-count-overflow
-Wfrontend-loop-interchange                        -Wno-missing-braces                                -Wshift-negative-value
-Wfunction-elimination                             -Wno-missing-declarations                          -Wshift-overflow
-Whsa                                              -Wno-missing-field-initializers                    -Wshift-overflow=
-Wif-not-aligned                                   -Wno-missing-format-attribute                      -Wsign-compare
-Wignored-attributes                               -Wno-missing-include-dirs                          -Wsign-conversion
-Wignored-qualifiers                               -Wno-missing-noreturn                              -Wsign-promo
-Wimplicit                                         -Wno-missing-parameter-type                        -Wsized-deallocation
-Wimplicit-fallthrough                             -Wno-missing-profile                               -Wsizeof-array-argument
-Wimplicit-fallthrough=                            -Wno-missing-prototypes                            -Wsizeof-array-div
-Wimplicit-function-declaration                    -Wno-mudflap                                       -Wsizeof-pointer-div
-Wimplicit-int                                     -Wno-multichar                                     -Wsizeof-pointer-memaccess
-Wimplicit-interface                               -Wno-multiple-inheritance                          -Wspeculative
-Wimplicit-procedure                               -Wno-multistatement-macros                         -Wstack-protector
-Wimport                                           -Wno-namespaces                                    -Wstack-usage=
-Winaccessible-base                                -Wno-narrowing                                     -Wstrict-aliasing
-Wincompatible-pointer-types                       -Wno-nested-externs                                -Wstrict-aliasing=
-Winherited-variadic-ctor                          -Wnonnull                                          -Wstrict-null-sentinel
-Winit-list-lifetime                               -Wnonnull-compare                                  -Wstrict-overflow
-Winit-self                                        -Wno-no-alloca-larger-than                         -Wstrict-overflow=
-Winline                                           -Wno-no-alloc-size-larger-than                     -Wstrict-prototypes
-Wint-conversion                                   -Wno-noexcept                                      -Wstrict-selector-match
-Winteger-division                                 -Wno-noexcept-type                                 -Wstring-compare
-Wint-in-bool-context                              -Wno-no-frame-larger-than                          -Wstringop-overflow
-Wintrinsic-shadow                                 -Wno-no-larger-than                                -Wstringop-overflow=
-Wintrinsics-std                                   -Wno-nonnull                                       -Wstringop-overread
-Wint-to-pointer-cast                              -Wno-nonnull-compare                               -Wstringop-truncation
-Winvalid-imported-macros                          -Wno-non-template-friend                           -Wstudents
-Winvalid-memory-model                             -Wno-non-virtual-dtor                              -Wsubobject-linkage
-Winvalid-offsetof                                 -Wno-normalized                                    -Wsuggest-attribute=cold
-Winvalid-pch                                      -Wno-no-stack-usage                                -Wsuggest-attribute=const
-Wjump-misses-init                                 -Wno-no-vla-larger-than                            -Wsuggest-attribute=format
-Wl,                                               -Wno-NSObject-attribute                            -Wsuggest-attribute=malloc
-Wlarger-than-                                     -Wnon-template-friend                              -Wsuggest-attribute=noreturn
-Wlarger-than=                                     -Wno-null-dereference                              -Wsuggest-attribute=pure
-Wline-truncation                                  -Wnon-virtual-dtor                                 -Wsuggest-final-methods
-Wliteral-suffix                                   -Wno-objc-root-class                               -Wsuggest-final-types
-Wlogical-not-parentheses                          -Wno-odr                                           -Wsuggest-override
-Wlogical-op                                       -Wno-old-style-cast                                -Wsurprising
-Wlong-long                                        -Wno-old-style-declaration                         -Wswitch
-Wlto-type-mismatch                                -Wno-old-style-definition                          -Wswitch-bool
-Wmain                                             -Wno-openmp-simd                                   -Wswitch-default
-Wmaybe-uninitialized                              -Wno-overflow                                      -Wswitch-enum
-Wmemset-elt-size                                  -Wno-overlength-strings                            -Wswitch-outside-range
-Wmemset-transposed-args                           -Wno-overloaded-virtual                            -Wswitch-unreachable
-Wmisleading-indentation                           -Wno-override-init                                 -Wsync-nand
-Wmismatched-dealloc                               -Wno-override-init-side-effects                    -Wsynth
-Wmismatched-new-delete                            -Wno-overwrite-recursive                           -Wsystem-headers
-Wmismatched-tags                                  -Wno-packed                                        -Wtabs
-Wmissing-attributes                               -Wno-packed-bitfield-compat                        -Wtarget-lifetime
-Wmissing-braces                                   -Wno-packed-not-aligned                            -Wtautological-compare
-Wmissing-declarations                             -Wno-padded                                        -Wtemplates
-Wmissing-field-initializers                       -Wno-parentheses                                   -Wterminate
-Wmissing-format-attribute                         -Wno-pedantic                                      -Wtraditional
-Wmissing-include-dirs                             -Wno-pedantic-cast                                 -Wtraditional-conversion
-Wmissing-noreturn                                 -Wno-pedantic-param-names                          -Wtrampolines
-Wmissing-parameter-type                           -Wno-pessimizing-move                              -Wtrigraphs
-Wmissing-profile                                  -Wno-placement-new                                 -Wtsan
-Wmissing-prototypes                               -Wno-pmf-conversions                               -Wtype-limits
-Wmudflap                                          -Wno-pointer-arith                                 -Wundeclared-selector
-Wmultichar                                        -Wno-pointer-compare                               -Wundef
-Wmultiple-inheritance                             -Wno-pointer-sign                                  -Wundefined-do-loop
-Wmultistatement-macros                            -Wno-pointer-to-int-cast                           -Wunderflow
-Wnamespaces                                       -Wno-pragmas                                       -Wuninitialized
-Wnarrowing                                        -Wno-prio-ctor-dtor                                -Wunknown-pragmas
-Wnested-externs                                   -Wno-property-assign-default                       -Wunreachable-code
-Wno-abi                                           -Wno-protocol                                      -Wunsafe-loop-optimizations
-Wno-abi-tag                                       -Wno-psabi                                         -Wunsuffixed-float-constants
-Wno-absolute-value                                -Wno-range-loop-construct                          -Wunused
-Wno-address                                       -Wno-realloc-lhs                                   -Wunused-but-set-parameter
-Wno-address-of-packed-member                      -Wno-realloc-lhs-all                               -Wunused-but-set-variable
-Wno-aggregate-return                              -Wno-real-q-constant                               -Wunused-const-variable
-Wno-aggressive-loop-optimizations                 -Wno-redundant-decls                               -Wunused-const-variable=
-Wno-aliasing                                      -Wno-redundant-move                                -Wunused-dummy-argument
-Wno-align-commons                                 -Wno-redundant-tags                                -Wunused-function
-Wno-aligned-new                                   -Wno-register                                      -Wunused-label
-Wno-all                                           -Wno-reorder                                       -Wunused-local-typedefs
-Wno-alloca                                        -Wno-restrict                                      -Wunused-macros
-Wno-alloca-larger-than                            -Wno-return-local-addr                             -Wunused-parameter
-Wno-alloca-larger-than=                           -Wno-return-type                                   -Wunused-result
-Wno-alloc-size-larger-than                        -Wnormalized                                       -Wunused-value
-Wno-alloc-size-larger-than=                       -Wnormalized=                                      -Wunused-variable
-Wno-alloc-zero                                    -Wnormalized=id                                    -Wuseless-cast
-Wno-ampersand                                     -Wnormalized=nfc                                   -Wuse-without-only
-Wno-analyzer-double-fclose                        -Wnormalized=nfkc                                  -Wvarargs
-Wno-analyzer-double-free                          -Wnormalized=none                                  -Wvariadic-macros
-Wno-analyzer-exposure-through-output-file         -Wno-scalar-storage-order                          -Wvector-operation-performance
-Wno-analyzer-file-leak                            -Wno-selector                                      -Wverbose-unbounded
-Wno-analyzer-free-of-non-heap                     -Wno-sequence-point                                -Wvexing-parse
-Wno-analyzer-malloc-leak                          -Wno-shadow                                        -Wvirtual-inheritance
-Wno-analyzer-mismatching-deallocation             -Wno-shadow-compatible-local                       -Wvirtual-move-assign
-Wno-analyzer-null-argument                        -Wno-shadow=compatible-local                       -Wvla
-Wno-analyzer-null-dereference                     -Wno-shadow=global                                 -Wvla-larger-than=
-Wno-analyzer-possible-null-argument               -Wno-shadow-ivar                                   -Wvla-parameter
-Wno-analyzer-possible-null-dereference            -Wno-shadow-local                                  -Wvolatile
-Wno-analyzer-shift-count-negative                 -Wno-shadow=local                                  -Wvolatile-register-var
-Wno-analyzer-shift-count-overflow                 -Wno-shift-count-negative                          -Wwrite-strings
-Wno-analyzer-stale-setjmp-buffer                  -Wno-shift-count-overflow                          -Wzero-as-null-pointer-constant
-Wno-analyzer-tainted-array-index                  -Wno-shift-negative-value                          -Wzero-length-bounds
-Wno-analyzer-too-complex                          -Wno-shift-overflow                                -Wzerotrip
-Wno-analyzer-unsafe-call-within-signal-handler    -Wno-sign-compare   





