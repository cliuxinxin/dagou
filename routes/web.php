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

Route::get('/home', 'HomeController@index');

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


