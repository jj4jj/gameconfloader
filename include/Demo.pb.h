// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: Demo.proto

#ifndef PROTOBUF_Demo_2eproto__INCLUDED
#define PROTOBUF_Demo_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2006000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2006000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_Demo_2eproto();
void protobuf_AssignDesc_Demo_2eproto();
void protobuf_ShutdownFile_Demo_2eproto();

class Demo;
class DemoTable;

// ===================================================================

class Demo : public ::google::protobuf::Message {
 public:
  Demo();
  virtual ~Demo();

  Demo(const Demo& from);

  inline Demo& operator=(const Demo& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Demo& default_instance();

  void Swap(Demo* other);

  // implements Message ----------------------------------------------

  Demo* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Demo& from);
  void MergeFrom(const Demo& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:
  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required uint32 id = 1;
  inline bool has_id() const;
  inline void clear_id();
  static const int kIdFieldNumber = 1;
  inline ::google::protobuf::uint32 id() const;
  inline void set_id(::google::protobuf::uint32 value);

  // required uint32 lv = 2;
  inline bool has_lv() const;
  inline void clear_lv();
  static const int kLvFieldNumber = 2;
  inline ::google::protobuf::uint32 lv() const;
  inline void set_lv(::google::protobuf::uint32 value);

  // optional string name = 3 [default = "this is a default value"];
  inline bool has_name() const;
  inline void clear_name();
  static const int kNameFieldNumber = 3;
  inline const ::std::string& name() const;
  inline void set_name(const ::std::string& value);
  inline void set_name(const char* value);
  inline void set_name(const char* value, size_t size);
  inline ::std::string* mutable_name();
  inline ::std::string* release_name();
  inline void set_allocated_name(::std::string* name);

  // optional string desc = 4;
  inline bool has_desc() const;
  inline void clear_desc();
  static const int kDescFieldNumber = 4;
  inline const ::std::string& desc() const;
  inline void set_desc(const ::std::string& value);
  inline void set_desc(const char* value);
  inline void set_desc(const char* value, size_t size);
  inline ::std::string* mutable_desc();
  inline ::std::string* release_desc();
  inline void set_allocated_desc(::std::string* desc);

  // @@protoc_insertion_point(class_scope:Demo)
 private:
  inline void set_has_id();
  inline void clear_has_id();
  inline void set_has_lv();
  inline void clear_has_lv();
  inline void set_has_name();
  inline void clear_has_name();
  inline void set_has_desc();
  inline void clear_has_desc();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::uint32 id_;
  ::google::protobuf::uint32 lv_;
  static ::std::string* _default_name_;
  ::std::string* name_;
  ::std::string* desc_;
  friend void  protobuf_AddDesc_Demo_2eproto();
  friend void protobuf_AssignDesc_Demo_2eproto();
  friend void protobuf_ShutdownFile_Demo_2eproto();

  void InitAsDefaultInstance();
  static Demo* default_instance_;
};
// -------------------------------------------------------------------

class DemoTable : public ::google::protobuf::Message {
 public:
  DemoTable();
  virtual ~DemoTable();

  DemoTable(const DemoTable& from);

  inline DemoTable& operator=(const DemoTable& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const DemoTable& default_instance();

  void Swap(DemoTable* other);

  // implements Message ----------------------------------------------

  DemoTable* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const DemoTable& from);
  void MergeFrom(const DemoTable& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:
  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // repeated .Demo list = 1;
  inline int list_size() const;
  inline void clear_list();
  static const int kListFieldNumber = 1;
  inline const ::Demo& list(int index) const;
  inline ::Demo* mutable_list(int index);
  inline ::Demo* add_list();
  inline const ::google::protobuf::RepeatedPtrField< ::Demo >&
      list() const;
  inline ::google::protobuf::RepeatedPtrField< ::Demo >*
      mutable_list();

  // @@protoc_insertion_point(class_scope:DemoTable)
 private:

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::RepeatedPtrField< ::Demo > list_;
  friend void  protobuf_AddDesc_Demo_2eproto();
  friend void protobuf_AssignDesc_Demo_2eproto();
  friend void protobuf_ShutdownFile_Demo_2eproto();

  void InitAsDefaultInstance();
  static DemoTable* default_instance_;
};
// ===================================================================


// ===================================================================

// Demo

// required uint32 id = 1;
inline bool Demo::has_id() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Demo::set_has_id() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Demo::clear_has_id() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Demo::clear_id() {
  id_ = 0u;
  clear_has_id();
}
inline ::google::protobuf::uint32 Demo::id() const {
  // @@protoc_insertion_point(field_get:Demo.id)
  return id_;
}
inline void Demo::set_id(::google::protobuf::uint32 value) {
  set_has_id();
  id_ = value;
  // @@protoc_insertion_point(field_set:Demo.id)
}

// required uint32 lv = 2;
inline bool Demo::has_lv() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Demo::set_has_lv() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Demo::clear_has_lv() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Demo::clear_lv() {
  lv_ = 0u;
  clear_has_lv();
}
inline ::google::protobuf::uint32 Demo::lv() const {
  // @@protoc_insertion_point(field_get:Demo.lv)
  return lv_;
}
inline void Demo::set_lv(::google::protobuf::uint32 value) {
  set_has_lv();
  lv_ = value;
  // @@protoc_insertion_point(field_set:Demo.lv)
}

// optional string name = 3 [default = "this is a default value"];
inline bool Demo::has_name() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void Demo::set_has_name() {
  _has_bits_[0] |= 0x00000004u;
}
inline void Demo::clear_has_name() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void Demo::clear_name() {
  if (name_ != _default_name_) {
    name_->assign(*_default_name_);
  }
  clear_has_name();
}
inline const ::std::string& Demo::name() const {
  // @@protoc_insertion_point(field_get:Demo.name)
  return *name_;
}
inline void Demo::set_name(const ::std::string& value) {
  set_has_name();
  if (name_ == _default_name_) {
    name_ = new ::std::string;
  }
  name_->assign(value);
  // @@protoc_insertion_point(field_set:Demo.name)
}
inline void Demo::set_name(const char* value) {
  set_has_name();
  if (name_ == _default_name_) {
    name_ = new ::std::string;
  }
  name_->assign(value);
  // @@protoc_insertion_point(field_set_char:Demo.name)
}
inline void Demo::set_name(const char* value, size_t size) {
  set_has_name();
  if (name_ == _default_name_) {
    name_ = new ::std::string;
  }
  name_->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:Demo.name)
}
inline ::std::string* Demo::mutable_name() {
  set_has_name();
  if (name_ == _default_name_) {
    name_ = new ::std::string(*_default_name_);
  }
  // @@protoc_insertion_point(field_mutable:Demo.name)
  return name_;
}
inline ::std::string* Demo::release_name() {
  clear_has_name();
  if (name_ == _default_name_) {
    return NULL;
  } else {
    ::std::string* temp = name_;
    name_ = const_cast< ::std::string*>(_default_name_);
    return temp;
  }
}
inline void Demo::set_allocated_name(::std::string* name) {
  if (name_ != _default_name_) {
    delete name_;
  }
  if (name) {
    set_has_name();
    name_ = name;
  } else {
    clear_has_name();
    name_ = const_cast< ::std::string*>(_default_name_);
  }
  // @@protoc_insertion_point(field_set_allocated:Demo.name)
}

// optional string desc = 4;
inline bool Demo::has_desc() const {
  return (_has_bits_[0] & 0x00000008u) != 0;
}
inline void Demo::set_has_desc() {
  _has_bits_[0] |= 0x00000008u;
}
inline void Demo::clear_has_desc() {
  _has_bits_[0] &= ~0x00000008u;
}
inline void Demo::clear_desc() {
  if (desc_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    desc_->clear();
  }
  clear_has_desc();
}
inline const ::std::string& Demo::desc() const {
  // @@protoc_insertion_point(field_get:Demo.desc)
  return *desc_;
}
inline void Demo::set_desc(const ::std::string& value) {
  set_has_desc();
  if (desc_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    desc_ = new ::std::string;
  }
  desc_->assign(value);
  // @@protoc_insertion_point(field_set:Demo.desc)
}
inline void Demo::set_desc(const char* value) {
  set_has_desc();
  if (desc_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    desc_ = new ::std::string;
  }
  desc_->assign(value);
  // @@protoc_insertion_point(field_set_char:Demo.desc)
}
inline void Demo::set_desc(const char* value, size_t size) {
  set_has_desc();
  if (desc_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    desc_ = new ::std::string;
  }
  desc_->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:Demo.desc)
}
inline ::std::string* Demo::mutable_desc() {
  set_has_desc();
  if (desc_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    desc_ = new ::std::string;
  }
  // @@protoc_insertion_point(field_mutable:Demo.desc)
  return desc_;
}
inline ::std::string* Demo::release_desc() {
  clear_has_desc();
  if (desc_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    return NULL;
  } else {
    ::std::string* temp = desc_;
    desc_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    return temp;
  }
}
inline void Demo::set_allocated_desc(::std::string* desc) {
  if (desc_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    delete desc_;
  }
  if (desc) {
    set_has_desc();
    desc_ = desc;
  } else {
    clear_has_desc();
    desc_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  // @@protoc_insertion_point(field_set_allocated:Demo.desc)
}

// -------------------------------------------------------------------

// DemoTable

// repeated .Demo list = 1;
inline int DemoTable::list_size() const {
  return list_.size();
}
inline void DemoTable::clear_list() {
  list_.Clear();
}
inline const ::Demo& DemoTable::list(int index) const {
  // @@protoc_insertion_point(field_get:DemoTable.list)
  return list_.Get(index);
}
inline ::Demo* DemoTable::mutable_list(int index) {
  // @@protoc_insertion_point(field_mutable:DemoTable.list)
  return list_.Mutable(index);
}
inline ::Demo* DemoTable::add_list() {
  // @@protoc_insertion_point(field_add:DemoTable.list)
  return list_.Add();
}
inline const ::google::protobuf::RepeatedPtrField< ::Demo >&
DemoTable::list() const {
  // @@protoc_insertion_point(field_list:DemoTable.list)
  return list_;
}
inline ::google::protobuf::RepeatedPtrField< ::Demo >*
DemoTable::mutable_list() {
  // @@protoc_insertion_point(field_mutable_list:DemoTable.list)
  return &list_;
}


// @@protoc_insertion_point(namespace_scope)

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_Demo_2eproto__INCLUDED
