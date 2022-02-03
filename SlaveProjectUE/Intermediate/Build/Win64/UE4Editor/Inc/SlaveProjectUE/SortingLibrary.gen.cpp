// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "SlaveProjectUE/SortingLibrary.h"
#ifdef _MSC_VER
#pragma warning (push)
#pragma warning (disable : 4883)
#endif
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeSortingLibrary() {}
// Cross Module References
	SLAVEPROJECTUE_API UClass* Z_Construct_UClass_USortingLibrary_NoRegister();
	SLAVEPROJECTUE_API UClass* Z_Construct_UClass_USortingLibrary();
	ENGINE_API UClass* Z_Construct_UClass_UBlueprintFunctionLibrary();
	UPackage* Z_Construct_UPackage__Script_SlaveProjectUE();
// End Cross Module References
	void USortingLibrary::StaticRegisterNativesUSortingLibrary()
	{
	}
	UClass* Z_Construct_UClass_USortingLibrary_NoRegister()
	{
		return USortingLibrary::StaticClass();
	}
	struct Z_Construct_UClass_USortingLibrary_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UE4CodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_USortingLibrary_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_UBlueprintFunctionLibrary,
		(UObject* (*)())Z_Construct_UPackage__Script_SlaveProjectUE,
	};
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_USortingLibrary_Statics::Class_MetaDataParams[] = {
		{ "Comment", "/**\n * \n */" },
		{ "IncludePath", "SortingLibrary.h" },
		{ "ModuleRelativePath", "SortingLibrary.h" },
	};
#endif
	const FCppClassTypeInfoStatic Z_Construct_UClass_USortingLibrary_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<USortingLibrary>::IsAbstract,
	};
	const UE4CodeGen_Private::FClassParams Z_Construct_UClass_USortingLibrary_Statics::ClassParams = {
		&USortingLibrary::StaticClass,
		nullptr,
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		nullptr,
		nullptr,
		UE_ARRAY_COUNT(DependentSingletons),
		0,
		0,
		0,
		0x001000A0u,
		METADATA_PARAMS(Z_Construct_UClass_USortingLibrary_Statics::Class_MetaDataParams, UE_ARRAY_COUNT(Z_Construct_UClass_USortingLibrary_Statics::Class_MetaDataParams))
	};
	UClass* Z_Construct_UClass_USortingLibrary()
	{
		static UClass* OuterClass = nullptr;
		if (!OuterClass)
		{
			UE4CodeGen_Private::ConstructUClass(OuterClass, Z_Construct_UClass_USortingLibrary_Statics::ClassParams);
		}
		return OuterClass;
	}
	IMPLEMENT_CLASS(USortingLibrary, 99398628);
	template<> SLAVEPROJECTUE_API UClass* StaticClass<USortingLibrary>()
	{
		return USortingLibrary::StaticClass();
	}
	static FCompiledInDefer Z_CompiledInDefer_UClass_USortingLibrary(Z_Construct_UClass_USortingLibrary, &USortingLibrary::StaticClass, TEXT("/Script/SlaveProjectUE"), TEXT("USortingLibrary"), false, nullptr, nullptr, nullptr);
	DEFINE_VTABLE_PTR_HELPER_CTOR(USortingLibrary);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
#ifdef _MSC_VER
#pragma warning (pop)
#endif
