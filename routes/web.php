<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', 'ItemsController@index');

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');

#Scrape
Route::get('/scrape', 'ScrapController@index')->name('scrape');

#Hospital
Route::get('/hospital', 'ItemsController@hospital')->name('hospital');

#Group
Route::get('/group', 'GroupsController@index')->name('group');
Route::post('/group', 'GroupsController@store')->name('groupStore');

#GroupDetal
Route::get('/group_detail/{group}', 'GroupDetailController@index')->name('groupDetail');
Route::post('/group_detail/{group}', 'GroupDetailController@store')->name('groupDetailStore');

#Profile
Route::get('/profiles/update', 'ProfilesController@update')->name('profilesUpdate');
Route::post('/profiles', 'ProfilesController@store')->name('profileStore');

#Book
Route::get('/books', 'BooksController@index')->name('books');
Route::get('/books/{user_id}', 'BooksController@userBooks')->name('userBooks');
Route::get('/book/{book_id}', 'BooksController@bookDetail')->name('bookDetail');
Route::post('/books', 'BooksController@store')->name('bookStore');

#Lending Record
Route::post('/lending_record', 'LendingRecordsController@store')->name('lendingRecordStore');
Route::post('/lending_record/update', 'LendingRecordsController@update')->name('lendingRecordUpdate');


