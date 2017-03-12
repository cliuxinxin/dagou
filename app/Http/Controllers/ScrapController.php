<?php

namespace App\Http\Controllers;

use App\Scrap;
use Illuminate\Http\Request;

class ScrapController extends Controller
{
    //
    public function index()
    {
        $scraps = Scrap::all();
        return view('index',compact('scraps'));
    }

}
